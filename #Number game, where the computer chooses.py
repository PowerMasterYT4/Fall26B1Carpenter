#Number game, where the computer chooses a nmumber 1 - 100 and
#the user has 10 guesses. and count the number of tries 

import random

number = random.randint(1, 100)
tries = 0

print("Guess a number from 1 to 100.")
print("You have 10 tries!")

while tries < 10:
    guess = int(input("Enter your guess: "))
    tries = tries + 1

    if guess == number:
        print("You got it!")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")

if tries == 10 and guess != number:
    print("You ran out of tries!")
    print("The number was", number)