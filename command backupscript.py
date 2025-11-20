import os
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

# ---------- File Inputs (using raw strings) ----------
DEVICE_FILE = r"C:\Users\username\Desktop\Python scripts\Device Config Backup\Backing UP\devices.txt"
CREDENTIAL_FILE = r"C:\Users\username\Desktop\Python scripts\Device Config Backup\Backing UP\credentials.txt"
COMMAND_FILE = r"C:\Users\username\Desktop\Python scripts\Device Config Backup\Backing UP\commands.txt"
OUTPUT_DIR = "outputs"

# ---------- Load Inputs ----------
try:
    with open(DEVICE_FILE) as f:
        devices = [line.strip() for line in f if line.strip()]

    with open(CREDENTIAL_FILE) as f:
        creds = f.read().strip().split(":")
        USERNAME, PASSWORD = creds[0], creds[1]

    with open(COMMAND_FILE) as f:
        commands = [line.strip() for line in f if line.strip()]

except FileNotFoundError as e:
    print(f"Error: Required file not found. {e}")
    exit(1)

# ---------- Ensure Output Directory ----------
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# ---------- Worker Function (Optimized) ----------
def collect_outputs(host):
    device = {
        "device_type": "cisco_ios",
        "host": host,
        "username": USERNAME,
        "password": PASSWORD,
    }
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(OUTPUT_DIR, f"{host}_{timestamp}.txt")
    
    # Combine all commands into a single string for efficiency
    all_commands_str = ' ; '.join(commands)

    try:
        with ConnectHandler(**device) as conn:
            conn.enable()
            print(f"[CONNECTED] Successfully connected to {host}")
            
            # Disable paging once, at the start
            conn.send_command("terminal length 0")

            # Use send_command for all commands, as it is faster for static output
            # Combining commands can be done, but a loop with send_command is often fine
            # as Netmiko handles the delays for individual commands reliably.
            with open(filename, "w", encoding="utf-8") as f:
                for cmd in commands:
                    f.write(f"\n\n<------ {cmd} ----->\n")
                    output = conn.send_command(cmd)
                    f.write(output)

        return f"[SUCCESS] {host} -> {filename}"
    
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as e:
        return f"[FAILED] {host} -> Connection error: {str(e)}"
    except Exception as e:
        return f"[FAILED] {host} -> General error: {str(e)}"

# ---------- Multi-thread Execution (Optimized) ----------
def main():
    print(f"Starting backup for {len(devices)} devices...")
    results = []
    # Use a maximum number of threads. 10 is a safe starting point.
    max_threads = 10 
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(collect_outputs, host): host for host in devices}
        for future in as_completed(futures):
            results.append(future.result())

    print("\n" + "="*40)   # Update the thread based on the requirement
    print("Backup Results")
    print("="*40)
    print("\n".join(results))
    print("\n" + "="*40)

if __name__ == "__main__":
    main()
