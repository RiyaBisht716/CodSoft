import random
import string

length =int(input("Enter the length: "))
chars= string.ascii_letters
chars+=string.digits
chars+=string.punctuation
password=""
for i in range(length):
    next_character = random.choice(chars)
    password+= next_character
print("Your new random password is: ",password)
