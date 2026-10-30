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
remote_connection.send("show run | section eigrp\n")
remote_connection.send("conf terminal\n")
remote_connection.send("hostname Paramiko-Ashish\n")
remote_connection.send("interface loopback0\n")
remote_connection.send("ip address 100.1.1.1 255.255.255.255\n")
remote_connection.send("router eigrp 100\n")
remote_connection.send("no auto-summary\n")
remote_connection.send("network 0.0.0.0\n")
remote_connection.send("end\n")
remote_connection.send("show run | section eigrp\n")

time.sleep(1)

output = remote_connection.recv(18999).decode('ascii')
print(output)
ssh_client.close