 #file ops
'''
Backup = open("config.txt","r")
print(Backup.read())
'''
from netmiko import ConnectHandler
import getpass

with open('device.txt','r') as hostname:
    devcies = hostname.read().splitlines()

for IP in devcies:
      
    cisco_01 = {
        "device_type": "cisco_ios",
        "host": IP,
        "username": "cisco",
        "password": "123456789", # Log in password from getpass
        'port': 22,
        "secret": "123456789" # Enable password from getpass
    }

    connection = ConnectHandler(**cisco_01)
    connection.enable()  #Moving in Enable Mode


    output = connection.send_command('show run')
    print(output)
    prompt = connection.find_prompt()
    print(prompt)
    hostname = prompt[0:-1]
    print(hostname)


    DeviceBackup = f'C:\\Users\\v s lishara\\Music\\Network Automation\\{hostname}-backup.txt'

    with open(DeviceBackup,'w') as backup:
        backup.write(output)
        print(f'Backup of {hostname} done')
        print('#'*30)
    print('Closing Connection')
    connection.disconnect()
