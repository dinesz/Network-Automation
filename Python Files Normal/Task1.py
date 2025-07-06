'''
command = "Hello World"
output = command[2]
print(output)

print(len(command))

'''

'''
def find_first(string, char):# string and char are argument
    index = string.find(char)
    return index


string = input("Enter the string: ")
char = input("Enter the character: ")

index = find_first(string, char)

#User input validation
if len(char) != 1:
    print("Enter the char to find")
else:
    index = find_first(string, char)

if index != -1:
    print(f"The first occurrence of '{char}' is at index {index}.")
else:
    print(f"The character '{char}' was not found ") 


'''
'''
string = "Hello World"

print(string[::2])



def remove_odd(string):
    return string[::2]


string = input("Enter the string: ")

odd_string = remove_odd(string)

print(f"The string after removing odd characters : {odd_string}")



evList = [3, 6, 9, 11, 13, 15, 17, 19]

#print(evList[::2])


for num in range(1,len(evList)):
    if num % 2 == 0: 
        print(evList[num])     


myDict={'x':250,'y':500,'z':410}

tolsum = 0

for val in myDict.values():
    tolsum += val;

print(tolsum)

#Remove particular key
myDict={'x':250,'y':500,'z':410}

remov_key = 'y'

if remov_key in myDict:
    del myDict[remov_key]
else:
    
    print("Key not found")
print("After removal:",myDict)


myDict={'x':250,'y':500,'z':410}

tolsum1 = 1

for val in myDict.values():
    tolsum1 *= val;

print(tolsum)

'''
