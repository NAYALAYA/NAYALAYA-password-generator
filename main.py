# Write your pseudocode first!

#Imports Here;
import random
import pyperclip

# Create an empty dictionary

webpass = {

}

#Ask for the website name

webby = input("What website is the password for?: ")

# Create list of letters

Pass = "abcdefghijklmnopqrstuvwzyz1234567890!?@#~$`;+=%&*-_/:<>|"

# Code that chooses 7 random Letters

randPass = random.choice(Pass)

randPass = ""

for let in range(12):
    randPass += random.choice(Pass)
print(f"Here is your password for {webby}: ", randPass)

# Copy New Password

pyperclip.copy(randPass)

# Tell the user about the copy

print("Your new password had been copied to the clipboard!\n")

# Add the website and password to dict

webpass[webby] = randPass


print("All passwords:")
print(webpass)

# Ask if they want to make another password

choice = input("Create another password? (y/n): ")

while choice == "y":
   
    webby = input("What website is the password for?: ")

    Pass = "abcdefghijklmnopqrstuvwzyz1234567890!?@#~$`;+=%&*-_/:<>|"

    randPass = random.choice(Pass)

    randPass = ""

    for let in range(12):
        randPass += random.choice(Pass)
    print(f"Here is your password for {webby}: ", randPass)

    pyperclip.copy(randPass)

    print("Your new password had been copied to the clipboard!\n")

    webpass[webby] = randPass


    print("All passwords:")
    print("", webpass, "\n")

    choice = input("Create another password? (y/n): ")

print ("All your passwords: ")

for webby, randPass in webpass.items():

    print(f"{webby}: {randPass}")

