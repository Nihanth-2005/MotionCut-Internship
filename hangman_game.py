import random

words = ["apple", "banana", "python", "biology", "computer"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("WELCOME TO HANGMAN")

while attempts > 0:
    print("Word:", " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong guess!")

    if "_" not in guessed:
        print("You found it!", word)
        break

    print(f"Remaining attempts: {attempts}")

if attempts == 0:
    print("You lost! The word was:", word)
