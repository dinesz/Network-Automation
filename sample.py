# Function to check if two strings are anagrams
#def anagrams(str1, str2):
    # Clean and sort the strings
    #str1 = ''.join(sorted(str1.replace(" ", "").lower()))
    #str2 = ''.join(sorted(str2.replace(" ", "").lower()))
str1 = aruba
str2 = uraba
Output1 = sorted(str1)
Output2 = sorted(str2)
    
    # Compare the sorted strings
    #return str1 == str2

    

# Main program
#str1 = input("Enter the first string: ")
#str2 = input("Enter the second string: ")

#if anagrams(str1, str2):
if Output1 == Output2:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
