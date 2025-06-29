from napalm import get_network_driver


driver = get_network_driver('ios')


switch_01 = {
    "hostname": '192.168.1.12',
    "username": "cisco",
    "password": "123456789",
    "optional_args":{"secret":"123456789"}
    }


device = driver(**switch_01)
device.open()
print("Connected successfully")


#device.load_merge_candidate(config='interface loopback10\n ip address 192.168.100.1 255.255.255.0')
device.load_merge_candidate(filename="iproute.txt")




print(device.compare_config())
if len(device.compare_config()) > 0:
    choice = input("\nWould you like to commit these changes? [yN]: ")
    if choice == 'y':
        print("Committing ....")
        device.commit_config()
        choice = input("\nWould you like to Rollback to previous config? [yN]: ")
        if choice == 'y':
            print("Rolling back to previous config ...")
            device.rollback()
    else:
        print("Discarding ...")
        device.discard_config()
else:
    print("No difference")
device.close()
print("Disconnected from the device")