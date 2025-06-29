from netmiko import ConnectHandler
from getpass import getpass

R2 = '192.168.1.10'
R3 = '192.168.1.11'
#R3 = '192.168.247.146'

Router_list = [R2, R3]

Username = input('Please Enter The username: ')
Password = input('Please Enter The Password: ')


def inter_conf():
    inter_name = input('Enter Your Interface Name: ')
    ip_address = input('Enter Your IP address: ')
    sub_mask = input('Enter Your Subnet Mask: ')

    commands = ['interface ' + inter_name, 'ip address ' + ip_address + ' ' + sub_mask, 'no shutdown']
    loopback = SSH.send_config_set(commands)
    print(loopback)

    inter_show = SSH.send_command('sh ip inter bri')
    print(inter_show)


def eigrp():
    eigrp_as_num = input('Enter Your AS Number ID: ')
    eigrp_network_count = int(input('How Many Network To Advertise: '))

    for network in range(0, eigrp_network_count):
        eigrp_network_id = input('Enter Your Network ID: ')
        eigrp_wild_mask = input('Enter The Wildcard Mask:')

        command = ['router eigrp ' + eigrp_as_num, 'network ' + eigrp_network_id + ' ' + eigrp_wild_mask]
        eigrp_config = SSH.send_config_set(command)
        print(eigrp_config)


def acl():
    acl_permit_network = input('Enter The Permit Network: ')
    subnet_mask = input('Enter The Network Subnet Mask: ')

    command = ['access-list 1 permit ' + acl_permit_network + ' ' + subnet_mask, 'interface lo20 ',
               'ip access-group 1 in']

    acl_config = SSH.send_config_set(command)
    print(acl_config)



def fetch_show_config():
    print('\n')
    print('#' * 20 + 'Interface Brief' + '#' * 20)
    int_brief = SSH.send_command('sh ip inter bri')
    print(int_brief + '\n')
    print('#'*20 + 'show ACL' + '#'*20)
    acl_show = SSH.send_command('show access-lists ' + '\n')
    print(acl_show)
    print('#' * 20 + 'show IP Protocol' + '#' * 20)
    show_ip_protocol = SSH.send_command('show ip protocols ' + '\n')
    print(show_ip_protocol)
    print('#' * 20 + 'show IP Route' + '#' * 20)
    show_route = SSH.send_command('show ip route ' + '\n')
    print(show_route)
    print('#' * 20 + 'show EIGRP NEIGHBORS' + '#' * 20)
    show_eigrp = SSH.send_command('show ip eigrp neighbors ' + '\n')
    print(show_eigrp)
    print('#' * 75)

    my_save_file = open('C:\\Users\\ajay.ya\\PycharmProjects\\pythonProject1\\Config.txt', 'a')
    my_save_file.write(int_brief)
    my_save_file.write(acl_show)
    my_save_file.write(show_ip_protocol)
    my_save_file.write(show_route)
    my_save_file.write(show_eigrp)
    my_save_file.close()


User_Choise = input('Welcome to Config Utility\n1.Interface,'
                    'EIGRP and ACL Config\n2.Fetch Show Command\nPlease Enter Your Choose(1/2): ')

if User_Choise == '1':
    for router in Router_list:
        device_temp = {
            'device_type': 'cisco_ios',
            'host': router,
            'username': Username,
            'password': Password
        }
        SSH = ConnectHandler(**device_temp)
        print('#' * 75 + '\n' + 'Connecting To Router ' + router + '\n' + '#' * 75 + "\n")
        inter_conf()
        eigrp()
        acl()

elif User_Choise == '2':
    for router in Router_list:
        device_temp = {
            'device_type': 'cisco_ios',
            'host': router,
            'username': Username,
            'password': Password
        }
        SSH = ConnectHandler(**device_temp)
        print('#' * 75 + '\n' + 'Connecting To Router ' + router + '\n' + '#' * 75 + "\n")
        fetch_show_config()


else:
    print('Invalid Input Detection\nPlease Try Again\nThank You...!!!')