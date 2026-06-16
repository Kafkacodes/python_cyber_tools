import random
import string

password_length = int(input("Enter the desired length of the password: "))
choice = input("Do you want to include special characters? (yes/no): ").strip().lower()

if choice == 'yes':
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    characters = string.ascii_letters + string.digits

password = ''.join(random.choice(characters) for _ in range(password_length))
print(f"Generated password: {password}")