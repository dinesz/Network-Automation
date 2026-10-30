from netmiko import ConnectHandler

ESW1 = {
"device_type" : "cisco_ios",
"ip" : "172.16.7.158",
"username" : "ashish",
"password" : "ashish",
"secret" : "gns3"
}
ESW2 = {
"device_type" : "cisco_ios",
"ip" : "172.16.7.159",
"username" : "ashish",
"password" : "ashish",
"secret" : "gns3"
}
ESW3 = {
"device_type" : "cisco_ios",
"ip" : "172.16.7.160",
"username" : "ashish",
"password" : "ashish",
"secret" : "gns3"
}
ESW4 = {
"device_type" : "cisco_ios",
"ip" : "172.16.7.161",
"username" : "ashish",
"password" : "ashish",
"secret" : "gns3"
}

list = [ESW1,ESW2,ESW3,ESW4]

for switch in list:
    print("Logging in to Switch**************")
    net_connect = ConnectHandler(**switch)
    net_connect.enable()

    for number in range (10,21,5):
        print("Creating Vlan " + str(number))
        config_commands = ["vlan " + str(number), "name Ashish_Vlan_" + str(number)]
        myoutput = net_connect.send_config_set(config_commands)
        print(myoutput)
print("I am done with the configuration on all devices")

net_connect.save_config()
