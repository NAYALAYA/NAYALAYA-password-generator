# Write your pseudocode first!

#Imports Here;
import random

# Create an empty dictionary

webpass = {

}

#Ask for the website name

webby = input("What website is the password for?: ")

# Create list of letters

Letters = "abcdefghijklmnopqrstuvwzyz"

# Code that chooses 7 random Letters

randLetters = random.choice(Letters)

randLetters = ""

for let in range(7):
    randLetters += random.choice(Letters)
print(randLetters)

# Create list of numbers

Numbers = "1234567890"

# Code that chooses 3 random numbers

randNumbers = random.choice(Numbers)

randNumbers = ""

for num in range(3):
    randNumbers += random.choice(Numbers)
print(randNumbers)

# Create list of characters

Characters = "!?@#~$`;+=%&*-_/:<>|"

# Code that chooses 2 random characters

randCharacters = random.choice(Characters)

randCharacters = ""

for char in range(2):
    randCharacters += random.choice(Characters)
print(randCharacters)

#


# Copy password