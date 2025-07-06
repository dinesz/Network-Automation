
'''
User = input("Enter user name: ")

if User == "Amith":
    print("You are authorized")
elif User == "Ajay":
    print("U r authorized")

else:
    print("U are not auth")
'''
'''
    
# If elif & else
a = 300
b = 40

if b>a:
    print("B is great")

elif a==b:
    print("a & b are equal ")

else:
    print("a is great")
'''
# multiple if condition
'''
x = 50

if x>20:
    print("x is above 20")
    if x>30:
        print(" x is above 30")
    else:
        print("but not above 30")
'''

#while example
'''
i =1 
while i<5:
    print(i)
    i = i+1
  '''  
# Print the list
''' 
Device = ["Cisco","Juniper","Arista","HPE"]

for i in Device:
    print(i)
    ''' 
'''
ip_list = ["192.168.10.10","192.168.10.11","192.168.10.3"]

for ip in ip_list:
    print(ip)
    '''

#range function
'''
range() 
function;
 
 '''

#tupple

IP_List = ["192.168.1.1","192.168.1.2","192.168.1.3"]

#ip address 192.168.1.1 255.255.255.255
#ip address 192.168.1.2 255.255.255.255
#ip address 192.168.1.3 255.255.255.255

Netmask = ("255.255.255.255","255.255.255.0","255.255.255.252") # Tuple
for ip in IP_List:
    for mask in Netmask:
        print(f"ip address {ip} {mask}")


'''
for ip in IP_List:
 for mask in Netmask:
  print(f"ip address {ip} {mask}")
  #Or print("ip address" +str(ip)+ str(mask))
'''

'''
# Concat strings
ip = 192
mask = 255
print(f"ip address {ip} {mask}") # Use this method for best practise
print("ip address " + str(ip)+" " +str(mask))
print("ip address {} {}".format(ip,mask))
'''