number = 100
guess = input('Guess: ')
guess = int(guess)
count = 1

while guess != number:
    if guess < number:
        guess = input('Guess higher: ')
    else:
        guess = input ('Guess lower: ')
    guess = int(guess)
    count = count + 1

if count > 3:
    print('You WIN on ' + str(count) + 'th try')
else:
    if count == 1:
        print('You WIN on ' + str(count) + 'st try')
    if count == 2:
        print('You WIN on ' + str(count) + 'nd try')
    if count == 3:
        print('You WIN on ' + str(count) + 'rd try')