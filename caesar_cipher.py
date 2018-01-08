#!/usr/bin/env python3
 
def ord26(ch):
    number = ord(ch) - 97
    return number


def chr26(n):
    letter = chr(n + 97) 
    return letter
    
    
def addchr(c1,c2):
    number = (ord26(c1) + ord26(c2)) % 26
    letter = chr26(number)
    return letter
    

def encr(key,m): 
    cipher = ''
    for i in m:
        if i == ' ':
            cipher = cipher + ' '
            continue
        cipher = '%s%s' % (cipher, addchr(key,i))
    
    return cipher
   
    
def subchr(c1,c2):
    number = (ord26(c2) - ord26(c1)) % 26
    letter = chr26(number)
    return letter
    
def decr(key,c):
    plain = ''
    for i in c:
        if i == ' ':
            plain = plain + ' '
            continue
        plain = '%s%s' % (plain, subchr(key,i))
    return plain                                                                                                                                                                                     




def main():
    while True:
        try:
            option = int(input("\nEnter an option:\n1: encrypt\n2: decrypt\n3: exit "))
        except ValueError:
            print("Invalid Input")
        else:
            if option == 1:
                message = input("Enter a message to encrypt: ")
                message = message.lower()
                key = input("Enter a key (any single character): ")
                message = encr(key,message)
                print(encr("s", message))

            elif option == 2:
                message = input("Enter a cipher to decrypt: ")
                message = message.lower()
                key = input("Enter the key (any single character): ")
                message = decr(key,message)
                print(decr("s",message))

            elif option == 3:
                break
                   

main()

