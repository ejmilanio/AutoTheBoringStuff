"""
Project: Number Guessing Game

1)Must generate a random number between 1-20
2)Must ask user input for guess
3)Give user 6 guesses
3)Must tell user if guess was higher or lower than answer


"""
import random

#create secret number
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

#give user 6 guesses
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is to high')
    else:
        print('This was it!')
        break #this is the win condition

if guess == secretNumber:
    print('Good job!')
else:
    print('Sorry. The number I was thinking of was ' + str(secretNumber))