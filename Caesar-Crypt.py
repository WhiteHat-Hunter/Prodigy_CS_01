# Caesar Cipher Encryption & Decryption Tool using Python By ~ Siddhesh Surve
# An Internship Based Task_1

import os

## Clear the console screen

if os.name == 'nt':
	os.system('cls')
else:
      os.system('clear')

print("\nInstalling Required Module...\n");

os.system("pip install pyfiglet")  ## Installing Required Module!

## Now, Making the program bit fnacy using pyfiglet for a banner on program launch

import pyfiglet

if os.name == 'nt':
	os.system('cls')
else:
      os.system('clear')

# Printing the figlet banner

if os.name == 'nt':
	fig = pyfiglet.figlet_format("Caeser-Crypt", font = "banner3-D", width = 80)
	print("\n")    
	print(fig)

	fig2 = pyfiglet.figlet_format("By - MR.SIDDHESH", font = "digital")
	print(fig2)
	print("\n")

else:
	fig = pyfiglet.figlet_format("Caesar-Crypt", font="standard", width=80)
	print("\n")    
	print(fig)

	fig2 = pyfiglet.figlet_format("By - MR.SIDDHESH", font = "standard")
	print(fig2)
	print("\n")

## Main Logic starts here, for Encryption & Decryption using Caeser Cipher Algorithm

def encrypt():
    text = input("\nEnter text to Encrypt > ")     # Prompt the user to Enter Message Text to Encryption
    key = int(input("\nEnter the Numerical key Value for Ceaser Encryption (eg: 1|2|3|...) > "))     # Prompt the user to Enter Key for Encryption

    cipher = (applyKey(text, key))
    
    print("\nEncrypted Ceaser Cipher Result > ", end="")
    
    for i in range(len(cipher)):
        print(cipher[i], end="")
    print()

def decrypt():
    cipher = input("\nEnter text to Decrypt > ")    # Prompt the user to Enter Message Text to Decryption
    key = int(input("\nEnter the Numerical key Value for Ceaser Decryption (eg: 1|2|3|...) > "))   # Prompt the user to Enter Key for Decryption

    text = (applyKey(cipher, -key))

    print("\nDecrypted Ceaser Cipher Result > ", end="")
    
    for i in range(len(text)):
        print(text[i], end="")
    print()
    
def applyKey(text, key):    # Applying Key to the text for Encyrption
    lst = []

    for i in range(len(text)):
        if inAlphabet(text[i]):
            lst.append(cycle(text[i], key))
        else:
            lst.append(text[i])

    return lst

def inAlphabet(char):       # Checking for Characters
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        return True
    return False

def cycle(char, key):   # Each Cycle to check for Characters & its Properties to Encrypt & Decrypt
    new = chr(ord(char) + key)

    if char >= 'a' and char <= 'z':
        capital = False
    else:
        capital = True

    if not inAlphabet(new):
        if capital:
            if new < 'A':
                new = chr(ord(new) + 26)
            else:
                new = chr(ord(new) - 26)
        else:
            if new < 'a':
                new = chr(ord(new) + 26)
            else:
                new = chr(ord(new) - 26)
    else:
        if not capital and new >= 'A' and new <= 'Z':
            new = chr(ord(new) + 26)
    return new

## Choose for Encryption or Decryption

Choice = int(input("Choose 1 for Encryption or 2 for Decryption >> "))

if Choice == 1:
    encrypt()
else:
    decrypt()

## Completion of Program Logic! Used a Common Logic such as loops & mathematical operation for Encryption & Decryption instead of using any third-party modules.
