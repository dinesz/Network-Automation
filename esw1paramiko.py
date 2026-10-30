import paramiko
import getpass
import time

HOST = input("Enter the IP Address of Router:")
username = input("Enter your username:")
password = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=HOST, username=username, password=password)

print("Successfully Connected\n")
remote_connection = ssh_client.invoke_shell()

remote_connection.send("configure terminal\n")
remote_connection.send("hostname Ashish-Switch\n")

for vlan in range(10,61,5):
    remote_connection.send("vlan " + str(vlan) + "\n")
    remote_connection.send("name Ashish_Paramiko_" + str(vlan) +"\n")

remote_connection.send("end\n")

time.sleep(8)
output = remote_connection.recv(18999).decode('ascii')
print(output)
ssh_client.close
