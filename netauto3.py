from netmiko import ConnectHandler
import getpass
pass_word = getpass.getpass("\n Enter the password: ")

device_1 = {
    "device_type":"cisco_ios", # Predefined command for cisco Change based on os type(XR, xe, ios)
    "host":"192.168.1.14",
    "username":"cisco",
    "password":pass_word
}

Connection = ConnectHandler(**device_1)
# Connection.enable()
# Connection.config_mode()


Outp= Connection.send_command("Sh ip route")


print(Outp)


Connection.disconnect()