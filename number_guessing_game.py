import random

number = random.randint(1, 50)
attempts = 10

print("Guess the number between 1 and 50")

for i in range(1, attempts + 1):
    guess = int(input("Enter your guess: "))

    if guess < 1 or guess > 50:
        print("Input must be between 1 and 50.")
        break

    if guess == number:
        print(f"Hurray! You guessed it right in {i} attempts.")
        break
    elif guess > number:
        if guess - number <= 3:
            print("Almost there!")
        elif guess - number <= 10:
            print("High!")
        else:
            print("Too high!")
    else:
        if number - guess <= 3:
            print("Almost there!")
        elif number - guess <= 10:
            print("Low!")
        else:
            print("Too low!")

    print(f"Remaining attempts: {attempts - i}")

if guess != number:
    print(f"You lost! The number was {number}")
