from netmiko import ConnectHandler
import csv
import time


Cisco_device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.10",
    "username": "cisco",
    "password": "123456789",

    "device_type": "cisco_ios",
    "host": "192.168.1.11",
    "username": "cisco",
    "password": "123456789",
}


Connection = ConnectHandler(**Cisco_device)
Connection.enable()  # Move to enable mode


output = Connection.send_command("show run","Show Version","Sh ip int brief")
print(output)


prompt = Connection.find_prompt()
hostname = prompt[0:-1]  


DeviceBackup = f"{hostname}-backup.csv"


with open(DeviceBackup, 'w', newline='') as backup:
    write = csv.writer(backup)
    write.writerow(["Command"])  
    for line in output.splitlines(): 
        write.writerow([line])  

print("Closing the connection")


Connection.disconnect() 
