from netmiko import ConnectHandler
#import getpass
from datetime import datetime
import time
import threading

start = time.time()

def backup(device):
    connection = ConnectHandler(**device)
    print("Entering to enable mode: ")
    connection.enable()

    output = connection.send_command('show run')
    
    prompt = connection.find_prompt()
    
    hostname = prompt[0:-1]
    
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hours= now.hour
    minute= now.minute


    DeviceBackup = f'C:\\Users\\v s lishara\\Music\\Network Automation\\{hostname}_{year}-{month}-{day}-{hours}-{minute}_backup.txt'

    with open(DeviceBackup,'w') as backup:
        backup.write(output)
        print(f'Backup of {hostname} done')
        print('#'*30)
    print('Closing Connection')
    connection.disconnect()

with open('device.txt','r') as hostname:
    devcies = hostname.read().splitlines()

threads = list()
for ip in devcies:
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "cisco",
        "password": "123456789"
    }

# creating a thread for each router that executes the backup function
    th = threading.Thread(target=backup, args=(device,))
    threads.append(th) # appending the thread to the list
for th in threads:
    th.start()

for th in threads:
    th.join()

end = time.time()
print(f'Total execution time:{end-start}')
