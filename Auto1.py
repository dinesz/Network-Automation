from netmiko import ConnectHandler

device_1 = {
    "device_type":"cisco_ios", # Predefined command for cisco Change based on os type(XR, xe, ios)
    "host":"192.168.1.14",
    "username":"cisco",
    "password":"123456789",
}

# Establish connection
Connection = ConnectHandler(**device_1)

Connection.config_mode()
Connection.send_command("ntp server 192.168.10.1")
Connection.exit_config_mode()
Output = Connection.send_command("Show run")
print(Output)

Connection.disconnect()
