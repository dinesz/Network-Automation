from netmiko import ConnectHandler

router1 = {
"device_type" : "cisco_ios",
"ip" : "172.16.7.158",
"username" : "ashish",
"password" : "ashish",
"secret" : "gns3"
}

net_connect = ConnectHandler(**router1)
net_connect.enable()

myoutput = net_connect.send_command("show vlan-switch brief")
print(myoutput)

for number in range (10,71,5):
    print("Creating Vlan " + str(number))
    config_commands = ["vlan " + str(number), "name Ashish_Vlan_" + str(number)]
    myoutput = net_connect.send_config_set(config_commands)
    print(myoutput)


net_connect.save_config()
