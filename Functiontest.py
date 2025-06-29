# Function is a block of code only run when it get call
#def keyword used to create function

def Dines(device): # device is argument
    #print(" Hello world")
    print(device+" Vendor ")

    Vendor_List = ["Cisco","Juniper","Arista"]

    for device in Vendor_List:
        Dines(device)

#Dines("Cisco") # Function call

#Dines("Juniper")