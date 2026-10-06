# Write your pseudocode first!

#Imports Here;
import random
import pyperclip

# Create an empty dictionary

webpass = {

}

choice = "y"

while choice == "y":
   
    webby = input("What website is the password for?: ")

    Pass = "abcdefghijklmnopqrstuvwzyz1234567890!?@#~$`;+=%&*-_/:<>|"

    randPass = random.choice(Pass)

    randPass = ""

    for let in range(12):
        randPass += random.choice(Pass)
    print(f"Here is your password for {webby}: ", randPass)

    pyperclip.copy(randPass)

    print("\nYour new password had been copied to the clipboard!\n")

    webpass[webby] = randPass

    print("All passwords: ")

    for webby, randPass in webpass.items():

     print(f"{webby}: {randPass}")


    choice = input("\nCreate another password? (y/n): ")

print ("\nAll your passwords: ")

for webby, randPass in webpass.items():

    print(f"{webby}: {randPass}")

