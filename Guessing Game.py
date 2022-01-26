# This program will give options to user for guessing a number .
# User should get 3 chances if the guess is correct it will be won or else lost.
number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_count += 1
    guess_number = int(input('Guess : '))
    if guess_number == number:
        print('You Won !!!')
        break
else:
    print('You Lost !!!')
