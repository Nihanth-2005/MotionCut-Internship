import random

comp_input = random.randint(1, 50)
rem_attempt = 10

for i in range(1, 11):
    user_input = int(input("Try to guess the number between 1 to 50: "))
    
    if user_input > 50 or user_input < 1:
        print("\n\nEntered input must be in between 1 to 50 !!")
        exit(0)
        
    rem_attempt -= 1
    
    if user_input == comp_input:
        print("\n\nHurray! You guessed it right in %d moves" % (i))
        break
        
    if user_input > comp_input:
        if (user_input - comp_input) > 10:
            print("Too high!")
        if (user_input - comp_input) < 10:
            if (user_input - comp_input) < 3:
                print("Almost there!")
            else:
                print("High!")
                
    if user_input < comp_input:
        if (comp_input - user_input) > 10:
            print("Too low!")
        if (comp_input - user_input) < 10:
            if (comp_input - user_input) < 3:
                print("Almost there!")
            else:
                print("Low!")
                
    print("Remaining attempts :%d\n\n " % (rem_attempt))
