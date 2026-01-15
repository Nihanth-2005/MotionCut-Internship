import random
import string

length = int(input("Enter password length: "))
choice = int(input("1. Digits\n2. Letters\n3. Letters + Digits\nChoose: "))

if choice == 1:
    chars = string.digits
elif choice == 2:
    chars = string.ascii_letters
else:
    chars = string.ascii_letters + string.digits

password = "".join(random.choice(chars) for _ in range(length))
print("Generated password:", password)
