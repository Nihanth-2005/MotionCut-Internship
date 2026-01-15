import random

print("!!WELCOME TO HANGMAN GAME!!")
print("Do you want to go through rules??\n\nIf yes, press 1 to continue. Else press 2: \n\n")

rule = int(input())
if rule == 1:
    print("Here are the rules of the game:")
    print("1. The game is played between a computer and a user")
    print("2. Upon selecting the difficulty, computer chooses a word at random")
    print("3. The user has to guess the word by suggesting letters, one at a time")
    print("4. If the user guesses a letter correctly, it will be displayed in the correct position")
    print("5. Maximum number of wrong guesses you can make is 6")
    print("ALL THE BEST!\n\n")

print("Choose Difficulty level(1-3): ")
print("1.Easy\n\n2.Medium\n\n3.Hard")
difficulty = int(input("Enter your choice: "))

if difficulty == 1:
    list1 = ["apple", "banana", "orange", "cat", "dog", "chair"]
    comp_choice1 = random.choice(list1)
    word = comp_choice1
    len1 = len(comp_choice1)
    print("_" * len1)
    start = "_" * len1
    max_wrong = 6
    wrongguess = 0
    while wrongguess != max_wrong:
        letter1 = input("Guess a letter: ")
        if len(letter1) != 1:
            print("Please enter a single letter")
        else:
            if letter1 in comp_choice1:
                print("Good guess")
                list_start = list(start)
                for i in range(len(word)):
                    if word[i] == letter1:
                        list_start[i] = letter1
                start = ''.join(list_start)
                print(start)
            else:
                print("Bad guess")
                wrongguess += 1
                print(start)
                print("Wrong guesses remaining: %d\n\n" % (max_wrong - wrongguess))
            if start == comp_choice1:
                print("You found it!")
                exit(0)
    print("You lost!!. The word is %s" % (word))

elif difficulty == 2:
    list2 = ["france", "india", "japan", "head", "heart", "salad"]
    comp_choice2 = random.choice(list2)
    word = comp_choice2
    len2 = len(comp_choice2)
    print("_" * len2)
    start = "_" * len2
    max_wrong = 6
    wrongguess = 0
    while wrongguess != max_wrong:
        letter2 = input("Guess a letter: ")
        if len(letter2) != 1:
            print("Please enter a single letter")
        else:
            if letter2 in comp_choice2:
                print("Good guess")
                list_start = list(start)
                for i in range(len(word)):
                    if word[i] == letter2:
                        list_start[i] = letter2
                start = ''.join(list_start)
                print(start)
            else:
                print("Bad guess")
                wrongguess += 1
                print(start)
                print("Wrong guesses remaining: %d\n\n" % (max_wrong - wrongguess))
            if start == comp_choice2:
                print("You found it!")
                exit(0)
    print("You lost!!. The word is %s" % (word))

elif difficulty == 3:
    list3 = ["freedom", "biology", "tennis", "piano", "basketball", "pyramids"]
    comp_choice3 = random.choice(list3)
    word = comp_choice3
    len3 = len(comp_choice3)
    print("_" * len3)
    start = "_" * len3
    max_wrong = 6
    wrongguess = 0
    while wrongguess != max_wrong:
        letter3 = input("Guess a letter: ")
        if len(letter3) != 1:
            print("Please enter a single letter")
        else:
            if letter3 in comp_choice3:
                print("Good guess")
                list_start = list(start)
                for i in range(len(word)):
                    if word[i] == letter3:
                        list_start[i] = letter3
                start = ''.join(list_start)
                print(start)
            else:
                print("Bad guess")
                wrongguess += 1
                print(start)
                print("Wrong guesses remaining: %d\n\n" % (max_wrong - wrongguess))
            if start == comp_choice3:
                print("You found it!")
                exit(0)
    print("You lost!!. The word is %s" % (word))

else:
    print("Select difficulty level between 1 to 3!")
