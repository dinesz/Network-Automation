from netmiko import ConnectHandler
import csv
import time

# Define the device details
Cisco_device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.10",
    "username": "cisco",
    "password": "123456789",
}

# Establish a connection to the device
try:
    Connection = ConnectHandler(**Cisco_device)
    Connection.enable()  # Move to enable mode
    print("Connected to the device successfully.")
except Exception as e:
    print(f"Failed to connect to the device: {e}")
    exit(1)

# List of commands to execute
commands = [
    "show run",
    "show version",
    "show ip interface brief",
]

# Get the hostname from the prompt
try:
    prompt = Connection.find_prompt()
    hostname = prompt[:-1]  # Slice off the '>' or '#' character from the prompt
except Exception as e:
    print(f"Failed to get the hostname: {e}")
    Connection.disconnect()
    exit(1)

# Define the backup filename
DeviceBackup = f"{hostname}-backup.csv"

# Write the output to the CSV file
try:
    with open(DeviceBackup, 'w', newline='') as backup:
        writer = csv.writer(backup)
        
        # Write a header
        writer.writerow(["Command", "Output"])
        
        for command in commands:
            try:
                output = Connection.send_command(command)
                print(f"Output for command '{command}':\n{output}\n")
                
                # Write command and its output to the CSV file
                writer.writerow([command])  # Write the command
                writer.writerow([output])   # Write the output
            except Exception as e:
                print(f"Failed to execute command '{command}': {e}")
                writer.writerow([command])  # Write the command
                writer.writerow(["Error executing command"])  # Write error message

    print("Data has been written to the CSV file successfully.")
except Exception as e:
    print(f"Failed to write data to the CSV file: {e}")

# Disconnect from the device
Connection.disconnect()
print("Connection closed.")
