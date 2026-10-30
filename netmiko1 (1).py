from netmiko import ConnectHandler

router1 = {
"device_type" : "cisco_ios",
"ip" : "172.16.7.153",
"username" : "ashish",
"password" : "ashish",
"secret" : "gns3"
}

net_connect = ConnectHandler(**router1)
net_connect.enable()

output = net_connect.send_command("show ip interface brief | include DHCP")
print(output)

config_commands = ["router ospf 100" , "network 0.0.0.0 0.0.0.0 area 0"]

output = net_connect.send_config_set(config_commands)

print(output)

net_connect.save_config()
