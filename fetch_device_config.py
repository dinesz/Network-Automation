import csv
import datetime
import os
from netmiko import ConnectHandler
from netmiko import NetMikoTimeoutException, NetMikoAuthenticationException
import textfsm

# Get the directory where the script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define all paths relative to the script location
commands_path = os.path.join(base_dir, "Commands.txt")
credentials_path = os.path.join(base_dir, "Credentials.txt")
hosts_path = os.path.join(base_dir, "Hosts.txt")
logs_dir = os.path.join(base_dir, "Logs")
latest_log_dir = os.path.join(base_dir, "Latest_Log")


def parse_output_with_textfsm(raw_output, template_path):
    with open(template_path) as template:
        fsm = textfsm.TextFSM(template)
        parsed_data = fsm.ParseText(raw_output)
    return parsed_data


def get_logs(host, uname, pass_wd, commands, log_folder):
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': uname,
        'password': pass_wd,
        'fast_cli': False
    }

    try:
        ssh = ConnectHandler(**device)
        print(f"Connected to {host}")
    except (NetMikoTimeoutException, NetMikoAuthenticationException):
        print(f"Connection to {host} failed.")
        return False

    hostname = ssh.find_prompt().strip('#')
    log_output = ""

    for command in commands:
        if not command.strip():
            continue
        output = ssh.send_command(command)
        log_output += f"{hostname}#{command}\n{output}\n\n"

    ssh.disconnect()

    ip_filename = f"{host}.txt"
    with open(os.path.join(log_folder, ip_filename), 'w') as f:
        f.write(log_output)
    with open(os.path.join(latest_log_dir, ip_filename), 'w') as f:
        f.write(log_output)

    print(f"Logs collected from: {host}")
    return True


def main():
    # Read commands
    try:
        with open(commands_path, 'r') as f:
            commands = f.read().splitlines()
    except FileNotFoundError:
        print("Commands.txt not found.")
        return

    # Read credentials
    try:
        with open(credentials_path, 'r') as f:
            creds = f.read().splitlines()
            username = creds[0]
            password = creds[1]
    except FileNotFoundError:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

    # Create folders
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H-%M-%S")
    log_folder = os.path.join(logs_dir, timestamp)
    os.makedirs(log_folder, exist_ok=True)
    os.makedirs(latest_log_dir, exist_ok=True)

    # Read hosts
    try:
        with open(hosts_path, 'r') as f:
            hosts = f.read().splitlines()
    except FileNotFoundError:
        print("Hosts.txt not found.")
        return

    # Clear Latest_Log folder
    for file_ in os.scandir(latest_log_dir):
        os.remove(file_.path)

    results = [["Host", "Successful Login"]]
    for host in hosts:
        if not host.strip():
            continue
        success = get_logs(host, username, password, commands, log_folder)
        results.append([host, "Yes" if success else "No"])

    # Write results to CSV
    with open(os.path.join(base_dir, "Results.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(results)


if __name__ == "__main__":
    import time
    start = time.perf_counter()
    main()
    print(f"Total time taken: {time.perf_counter() - start:.2f} seconds")