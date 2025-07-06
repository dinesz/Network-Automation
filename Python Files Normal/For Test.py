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
