from netmiko import ConnectHandler
import getpass
pass_word = getpass.getpass("\n Enter the password: ")

devices_1 = [
{
    "device_type":"cisco_ios", # Predefined command for cisco Change based on os type(XR, xe, ios)
    "host":"192.168.1.14",
    "username":"cisco",
    "password":pass_word
},
{
    "device_type":"cisco_ios", # Predefined command for cisco Change based on os type(XR, xe, ios)
    "host":"192.168.1.12",
    "username":"cisco",
    "password":pass_word
}
]

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
    "description Test_link1",
    "ip access-group 100 in",
    "no shutdown",
    "exit"
]

for device in devices_1:
    #try:
        Connection = ConnectHandler(**device)

        Output = Connection.send_config_set(Config_Command)
        print(f"Output from {device['host']}:\n{Output}\n")

        Connection.disconnect()
   # except Exception as e:
    #    print(f"An error occurred with device {device['host']}: {e}")    

