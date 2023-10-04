
# --------------------    TASK 02    --------------------

import random
import string

# Prompt User to Enter the Length of Password

length = int(input("Enter the length of the password to be generated : "))

# Prompt User to Enter the Complexity of Password

print("Choose the complexity of password :")
l = input("Include Lowercases ? (y/n) : ").lower()
u = input("Include Uppercase ? (y/n) : ").lower()
i = input("Include Integers ? (y/n) : ").lower()
s = input("Include Special Symbols ? (y/n) : ").lower()

# Generating Password

Lower_Characters = string.ascii_lowercase
Upper_Characters = string.ascii_uppercase
Integers = string.digits
Symbols = string.punctuation

complexity = ""

if l == 'y' :
    complexity = complexity + Lower_Characters

if u == 'y':
    complexity = complexity + Upper_Characters

if i == 'y' :
    complexity = complexity + Integers

if s == 'y' :
    complexity = complexity + Symbols

password = "".join(random.sample(complexity,length))

# Display Password

print(f"Your Generated Password Is : {password}")
