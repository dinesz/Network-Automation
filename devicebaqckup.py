
from napalm import get_network_driver
# from napalm.base import ConnectionException

driver = get_network_driver("ios")

switch_01 = {
    "hostname" : '192.168.1.12',
    "username" : 'cisco',
    "password" : '123456789',
    "optional_args" : {"secret":"123456789"}
    }

device = driver(**switch_01)
device.open()
print("connected successful")

print(f"Connecting to {switch_01['hostname']}")
output = device.get_config(retrieve="running")
print(output)

Run_Config = output['running']
print(Run_Config)

with open('bkp.txt','w') as backup:
    backup.write(Run_Config)
device.close()
print("device disconnected successful")

'''


from napalm import get_network_driver
# from napalm.base import ConnectionException

driver = get_network_driver("ios")

switch_01 = {
    "hostname": '192.168.1.12',
    "username": 'cisco',
    "password": '123456789',
    "optional_args": {"secret": "123456789"}
}

try:
    device = driver(**switch_01)
    device.open()
    print("Connected successfully to", switch_01['hostname'])

    output = device.get_config(retrieve="running")
    Run_Config = output['running']

    print(Run_Config)

    with open('bkp1.txt', 'w') as backup:
        backup.write(Run_Config)

except ConnectionException as e:
    print(f"Connection failed: {e}")
finally:
    device.close()
    print("Disconnected successfully")
'''