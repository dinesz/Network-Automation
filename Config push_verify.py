import os
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

# ---------- File Inputs ----------
DEVICE_FILE = r"C:\Users\userprofilename\Python scripts\Device Config Backup\Backing UP\devices.txt"
CREDENTIAL_FILE = r"C:\Users\userprofilename\Desktop\Python scripts\Device Config Backup\Backing UP\credentials.txt"
COMMAND_FILE = r"C:\Users\userprofilename\Desktop\Python scripts\Device Config Backup\Backing UP\config.txt"
OUTPUT_DIR = "outputs"

# ---------- Load Inputs ----------
try:
    with open(DEVICE_FILE) as f:  # Open the specified file in the Read mode and assign the file objects to variable f
        devices = [line.strip() for line in f if line.strip()]  #line.strip() removes front/back whitespace , if line.strip() ensures empty lines are ignored.

    with open(CREDENTIAL_FILE) as f:
        creds = f.read().strip().split(":")
        USERNAME, PASSWORD = creds[0], creds[1]
        ENABLE_SECRET = creds[2] if len(creds) > 2 else PASSWORD

    with open(COMMAND_FILE) as f: # Opens the file containing CLI commands
        commands = [line.strip() for line in f if line.strip()]

except FileNotFoundError as e:
    print(f"Error: Required file not found. {e}")
    exit(1)

# ---------- Ensure Output Directory ----------
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# ---------- Worker Function ----------
def push_and_verify(host):
    device = {
        "device_type": "cisco_ios",
        "host": host,
        "username": USERNAME,
        "password": PASSWORD, #Pcpey2@21
        "secret": ENABLE_SECRET
    }
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(OUTPUT_DIR, f"{host}_{timestamp}.txt")

    try:
        with ConnectHandler(**device) as conn:
            conn.enable()
            print(f"[CONNECTED] {host}")

            # Push configuration
            output = conn.send_config_set(commands)
            conn.save_config()  #Used to write the config. No need to put write command 

            # Validating the config
            verify_cmd = "show running-config | include file verify auto"
            verify_output = conn.send_command(verify_cmd)

            status = "[SUCCESS]" if "file verify auto" in verify_output else "[FAILED] Verification"
            
            # Write logs
            with open(filename, "w", encoding="utf-8") as f:
                f.write("=== CONFIG OUTPUT ===\n")
                f.write(output)
                f.write("\n\n=== VERIFICATION OUTPUT ===\n")
                f.write(verify_output)
                f.write(f"\n\nStatus: {status}")

        return f"{status} {host} -> {filename}"

    except (NetmikoTimeoutException, NetmikoAuthenticationException) as e:
        return f"[FAILED] {host} -> Connection error: {str(e)}"
    except Exception as e:
        return f"[FAILED] {host} -> General error: {str(e)}"

# ---------- Multi-thread Execution ----------
def main():
    print(f"Starting config push for {len(devices)} devices...")
    results = []
    max_threads = 20  # update thread count as per the requirement
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(push_and_verify, host): host for host in devices}
        for future in as_completed(futures):
            results.append(future.result())

    print("\n" + "="*40)
    print("Config Push Results")
    print("="*40)
    print("\n".join(results))
    print("\n" + "="*40)

if __name__ == "__main__":
    main()
