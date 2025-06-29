from netmiko import ConnectHandler
import getpass
pass_word = getpass.getpass("Enter the password: ")

device_1 = {
    "device_type":"cisco_ios", # Predefined command for cisco Change based on os type(XR, xe, ios)
    "host":"192.168.1.7",
    "username":"cisco",
    "password":pass_word
}

Connection = ConnectHandler(**device_1)
# Connection.enable()
# Connection.config_mode()
'''
Config_Command= ["interface fa0/0","desc Test_Wan","exit","access-list 10 permit any"]
'''

Config_Command = [
    "interface fa0/0",
    "description Test_Wan2",
    "exit",
    "access-list 10 permit any",
    "ip nat inside source list 10 interface fa0/0 overload",
    "ip access-list extended 100",
    "permit ip any any",
    "exit",
    "interface Ethernet1/0",
    "ip access-group 100 in",
    "no shutdown",
    "exit"
]

Output = Connection.send_config_set(Config_Command)
print(Output)

Connection.disconnect()

'''

from netmiko import ConnectHandler
import getpass
pass_word = getpass.getpass("Enter the password: ")

device_1 = {
    "device_type":"cisco_ios", # Predefined command for cisco Change based on os type(XR, xe, ios)
    "host":"192.168.1.6",
    "username":"cisco",
    "password": pass_word, # Log in password from getpass
    "secret": pass_word # Enable password from getpass
}


connection = ConnectHandler(**device_1)
connection.enable()  #Moving in Enable Mode


output = connection.send_command('show run')
print(output)
prompt = connection.find_prompt()
print(prompt)
hostname = prompt[0:-1]
print(hostname)

#0DeviceBackup = f'{hostname}-backup.txt'
DeviceBackup = f'C:\\Users\\v s lishara\\Music\\Network Automation\\{hostname}-backup.txt'


with open(DeviceBackup,'w') as backup:
     backup.write(output)
     print(f'Backup of {hostname} done')
     print('#'*30)
print('Closing Connection')
connection.disconnect()


'''

