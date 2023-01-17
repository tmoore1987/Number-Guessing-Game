import random

# generate random number and track how many times it take a user to guess it


secret_number = random.randint(1,11)
guesses = 0

while True:
    guesses +=1
    guess = int(input(' Please guess number between 1 and 10: '))
    if guess > secret_number:
        print('Please guess a number that is lower.')
    elif guess < secret_number:
        print('Please guess a number that is higher.')
    elif guess == secret_number:
        print('Congratulations! You guessed correctly!')
        print(f'Numbers of guesses was {guesses}.')
        play_again = input('Do you want to play again? (y/n) '). lower()
        if not play_again == "y":
            break

