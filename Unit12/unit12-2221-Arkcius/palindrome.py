"""
make palindrome
Author: Ryan Robison
"""

#palidrome takes in string
def palindrome(string):
    #vowel list
    vowel = ["a","e","i","o","u"]
    #odd and string two made
    odd = False
    string2 = ""
    #for loop to check for vowel and if vowel then makes odd true
    for i in range(len(vowel)):
        if string[len(string)-1] == vowel[i]:
            odd = True
    #if od true skips one and makes odd false and otehrwise makes string2 then ends of string
    for i in range(len(string)):
        if odd == True:
            odd = False
            continue
        else:
            i += 1
            string2 += string[len(string)-i] 
    #compine and return string and string 2
    stringer = string+string2
    return stringer

def main():
    #while input isnt blank prompts word and returns and prints palindrome of said word
    while True:
        string = input("Enter Word: ")
        if string == "":
            break
        print(palindrome(string))
    
main()