
#Date: February 9, 2021
#Name: Kubanychbek kyzy Aigerim
import random
from random import randint
user = input('Welcome to the game.\n Please enter your user name: ')
choice = True
while choice:
    guessed = False
    num_tries=0
    choice = input('Would you like to play?' + '\U0001F3B0' +' [yes] or [no]: ')
    if choice.lower() == 'no':
        print('You chose not to play, exiting...')
        choice = False
        break
    while choice !='yes' and choice!='no':
        choice = input('You must enter [yes] or [no]: ')
    range_ = input('Choose the range. Example: 0-50: ').split('-')
    secret_num = randint(int(range_[0]), int(range_[1]))
    print(f'You will have to guess a number between {int(range_[0])} and {int(range_[1])}')
    while not guessed:
        user_num = int(input('\U00002B50'+'Enter your guess: '))
        num_tries+=1
        if user_num == secret_num:
            print('\U00002714' +f'Congrats, {user.title()}!' + '\U0001F389')
            print(f'You needed just {num_tries} tries to guess the number. Yes, it was {secret_num}.\nGood bye!!!' + '\U0001F44B')
            break
        elif user_num > int(range_[1]) or user_num < int(range_[0]):
            print(f'Your number is out of range.')
            print(f'You will must guess a number between {int(range_[0])} and {int(range_[1])}')
            continue
        else:
            print('\U0000274C' + 'Oh no, your guess was wrong')
            if(num_tries>5):
                hint = input('Would you like a hint?'+ '\U0001F609' +'[yes] or [no]: ')
                if hint.lower() == 'yes':
                    if user_num - secret_num > 0:
                        print('\U0001F4A1'+'The secret number is smaller than '+ str(user_num))
                    else:
                        print('\U0001F4A1'+'The secret number is greater than '+ str(user_num))
        continue
