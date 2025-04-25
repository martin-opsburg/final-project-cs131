# martin burger
# burger_m@lynchburg.edu
# cs-131 final project
# v0.2 of game 2.3: Crack the Passcode

# importing random.mod for use with passcode generation
import random

def main():
    greating()
    mk_passcode()
    #get_guess()


## a simple welcome message
## that also outlines the rules
def greating():
    print('\n\t'
          'Welcome to ***Crack the Passcode!!!***\n\t'
          'You will have 10 chances to crack the code.\n\t'
          'The code length is 3 digits, and there will be no repeated numbers.\n\t'
          'After submitting your answer, you will then receive a clue.\n\t'
          'The clues are as follows.\n\t'
          'A RED card means that all digits were incorrect.\n\t'
          'A BLUE card means that one digit is correct but not in an incorrect position.\n\t'
          'A GREEN card means that one digit is correct and is in the correct position.\n\t'
          'Good LUCK!!!\n')

## time to generate a new passcode to be cracked
def mk_passcode():
    number_pool = (range(0,10))
    list_passcode = (random.sample(number_pool, 3)) 
    #print(f'JUST A TEST: {true_pc}') # this print() is here for function testing
    get_guess(list_passcode)    


def get_guess(list_passcode):
    print('What do you think the passcode is?')
    user_guess = input('> ')
    list_user = list(user_guess)
    check_score(list_user, list_passcode)

def check_score(list_user, list_passcode):
    print(list_user, list_passcode)
    #str_passcode = str(list_passcode[0]) + str(list_passcode[1]) + str(list_passcode[2])
    if list_user == list_passcode:
        print('Correct. You Win!')
    elif list_user[0] == list_passcode[0]:
        print('Green Card')
    elif list_user[1] == list_passcode[1]:
        print('Green Card')
    elif list_user[2] == list_passcode[2]:
        print('Green Card')
    else:
        for digit in list_user:
            if digit in list_passcode:
                print('Blue Card')
            if digit not in list_passcode is True:
                print('Red Card')
                break 


## simply calling the main function
main()
