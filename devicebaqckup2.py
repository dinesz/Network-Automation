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

device.load_merge_candidate(filename="bkp.txt")

print(device.compare_config())
if len(device.compare_config()) > 0:
    choice = input("\nWould you like to commit these changes? [Y/N]: ")
    if choice == 'y':
        print("comitting..")
        device.commit_config()
    else:
        print("Discarding..")
        device.discard_config()
else:
    print("No difference")

    device.close()
    print("Device Disconnected")