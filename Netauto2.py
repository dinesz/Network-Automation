from netmiko import ConnectHandler
import getpass
pass_word = getpass.getpass("Enter the password: ")

device_1 = {
    "device_type":"cisco_ios", # Predefined command for cisco Change based on os type(XR, xe, ios)
    "host":"192.168.1.6",
    "username":"cisco",
    "password":pass_word

     #"password":"123456789",
}

Connection = ConnectHandler(**device_1)
Show_Command = ["Sh ip route","Sh ip int bri","Sh clock","Sh ntp status"]
#Connection.disconnect()
for command in Show_Command:
    print(f"\n **Send command {command}***")
    output = Connection.send_command(command)
    print("\n",output)
 

Connection.disconnect()