from netmiko import ConnectHandler
import getpass
pass_word = getpass.getpass("Enter the password: ")

device_1 = {
    "device_type":"cisco_ios", # Predefined command for cisco Change based on os type(XR, xe, ios)
    "host":"192.168.1.14",
    "username":"cisco",
    "password":pass_word
}

Connection = ConnectHandler(**device_1)
# Connection.enable()
# Connection.config_mode()

#Config_Command= ["interface fa0/0","desc Test_Wan","exit","access-list 10 permit any"]

Config_Command = [
    "interface fa0/0",
    "description Test_Wan1",
    "exit",
    "access-list 10 permit any",
    "ip nat inside source list 10 interface fa0/0 overload",
    "ip access-list extended 100",
    "permit ip any any",
    "exit",
    "interface Ethernet1/0",
    "ip access-group 100 in",
    "exit"
]
Output = Connection.send_config_set(Config_Command)
print(Output)

Connection.disconnect()

