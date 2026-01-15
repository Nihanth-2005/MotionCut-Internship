import string
import random
import pyperclip

print("Choose an option:")
print("1.Generate a random password using all characters\n\n2.Generate a random password using selective criteria")

choiceinput = int(input())

if choiceinput == 1:
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        exit()
    res = ''.join(random.choices(string.printable, k=length))
    print("Generated random password:", res)

elif choiceinput == 2:
    try:
        print("Select an option for password generation:")
        print("1: Digits only")
        print("2: Punctuation only")
        print("3: Uppercase letters only")
        print("4: Lowercase letters only")
        print("5: Digits and punctuation")
        print("6: Digits and letters")
        print("7: Uppercase and lowercase letters")
        
        selectinput = int(input("Enter your choice (1-7): "))
        print("Enter password length: ")
        pwdlen = int(input())
        
        if selectinput == 1:
            res = ''.join(random.choices(string.digits, k=pwdlen))
        elif selectinput == 2:
            res = ''.join(random.choices(string.punctuation, k=pwdlen))
        elif selectinput == 3:
            res = ''.join(random.choices(string.ascii_uppercase, k=pwdlen))
        elif selectinput == 4:
            res = ''.join(random.choices(string.ascii_lowercase, k=pwdlen))
        elif selectinput == 5:
            res = ''.join(random.choices(string.digits + string.punctuation, k=pwdlen))
        elif selectinput == 6:
            res = ''.join(random.choices(string.digits + string.ascii_letters, k=pwdlen))
        elif selectinput == 7:
            res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=pwdlen))
        else:
            print("Enter value from given combinations!")
            res = "" # Initializing res to avoid errors later
            
        if res:
            print("Generated random password is:", res)
            
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        exit()
else:
    print("Choose a valid option!")
    exit()

print("Would you like to copy the password?")
print("1.Yes\n\n2.No")

try:
    user_input = int(input())
    if user_input == 1:
        pyperclip.copy(res)
        copied_text = pyperclip.paste()
        print("Copied password:", copied_text)
    else:
        print("Password not copied.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
