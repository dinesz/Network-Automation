'''
from netmiko import ConnectHandler
#import getpass
#pass_word = getpass.getpass("\n Enter the password: ")

my_device = {
    "device_type":"cisco_ios", # Predefined command for cisco Change based on os type(XR, xe, ios)
    "host":"192.168.1.14",
    "username":"cisco",
    "password":"123456789"
}

Connection = ConnectHandler(**my_device)

print("Connection successs")

Config = Connection.send_config_from_file(config_file="config.txt")

print(Config)

print(Connection.send_command("sh ip int brief"))

Connection.disconnect()

'''

from netmiko import ConnectHandler

Device_list = ["192.168.1.14","192.168.1.12"]

for device in Device_list:
   Cisco_divice= {
   "device_type":"cisco_ios",
   "host":device,
   "username":"cisco",
   "password":"123456789"
   }
   Command_list= ["show ip int bri","show ip route","sho clock","show ntp status"]
   print(f"\n{"#"*35}\n Connecting to device {Cisco_divice['host']}")
   Connection = ConnectHandler(**Cisco_divice)
   print(f"\n{"#"*35}\n Connected Successfully to device {Cisco_divice['host']}")


   for Command in Command_list:
       Output = Connection.send_command(Command)
       print(Output)

Connection.disconnect()
