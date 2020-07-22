import random

secretNumber = random.randint(1, 20)
print('i am thinking of a number between 1 and 20')

for guessTaken in range(1, 7):
    print('take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break

if guess == secretNumber:
    print('you guess the secret number in '+str(guessTaken)+' guesses')
else:
    print('no my secret number is '+str(secretNumber))


