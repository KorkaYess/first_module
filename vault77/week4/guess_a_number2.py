import random


hidden_number = random.randint(1, 100)


guess = input('Guess a number: ')
guess = int(guess)

def find(hidden_number, guess):
    while guess != 'quit':
        guess = int(guess)
        if guess < hidden_number:
            guess = input('Try higher or quit: ')
        elif guess > hidden_number:
            guess = input('Try lower or quit: ')
        elif guess == hidden_number:
            print('Congarulations, You found it!')
            return hidden_number
    print('Looser')
    
find(hidden_number, guess)