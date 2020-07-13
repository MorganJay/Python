secretNumber = 16
tries = 0
tries_limit = 6
while tries < tries_limit:
    guess = int(input('Guess the number: '))
    tries += 1
    if guess == secretNumber:
        print('You win!')
        break
else:
    print('Take your L in peace.')
