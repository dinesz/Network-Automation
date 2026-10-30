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

print ("Executing commands saved in eigrp.txt")

ashishoutput = net_connect.send_config_from_file("eigrp.txt")

print(ashishoutput)

net_connect.save_config()   
