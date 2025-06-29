from napalm import get_network_driver
import getpass


passwd = getpass.getpass("Please Enter the Password: ")
Driver = get_network_driver("ios")

Switch_01= {
    "hostname":"192.168.1.11",
    "username":"cisco",
    "password":passwd,
    "optional_args":{"secret":passwd}
}

Connection= Driver(**Switch_01)
Connection.open()   #Opens the connection to the network devics
print(f"Connectioning to {Switch_01["hostname"]}")

ouput = Connection.get_arp_table() # To fetch ARP table
print(ouput)
Connection.close()
