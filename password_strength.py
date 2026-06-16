password = input("Enter a password: ")

if len(password) > 8:
    print("Length is good.")
    
else:
    print("Too short.")

for char in password:
    if char.isupper():
        print("Contains uppercase letter.")
        break
else:    print("No uppercase letter found.")

for char in password:
    if char.islower():
        print("Contains lowercase letter.")
        break
else:    print("No lowercase letter found.")

for char in password:
    if char.isdigit():
        print("Contains a digit.")
        break
else:    print("No digit found.")

import string
for char in password:
    if char in string.punctuation:
        print("Contains a special character.")
        break
else:    print("No special character found.")

all_conditions_met = (len(password) > 8 and
                      any(char.isupper() for char in password) and
                      any(char.islower() for char in password) and
                      any(char.isdigit() for char in password) and
                      any(char in string.punctuation for char in password))

if all_conditions_met:
    print("Password is strong.")
else:    print("Password is weak.")
