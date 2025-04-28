# martin burger
# burger_m@lynchburg.edu
# cs-131 final project
# v0.3 of game 2.3: Crack the Passcode

### ToDo
#   0.  Write up better comments for each function
#   1.  Add some user.input.validation
#   2.  Wrap most of it up into a loop that
#           ends when user_digits == correct_digits is True
#           or 10 fatal attempts at guessing correct_digits
#   3.  Put some polish on it
#       [] remove unused functions
#       [] exception handling
#       [] improve the greeting print.format
#       [] review function names to make sure they make sense
#       [] 

# importing random.mod for use with passcode generation
import random

def main():
    greating()
    correct_string = str()
    correct_digits = list()
    mk_passcode(correct_string, correct_digits)
    user_tries = 0
    user_digits = list()
    user_string = str()
    cards = list()
    user_exp_loop(correct_digits, user_digits, cards, user_tries, user_string)
    
def user_exp_loop(correct_digits, user_digits, cards, user_tries, user_string):
    while user_tries <= 9:
        get_guess(user_digits, user_string)
        check_score(correct_digits, user_digits, cards)
        show_score(cards, user_tries)
        user_string = ""
        user_digits.clear()
        cards.clear()
        user_tries += 1

## a simple welcome message
## that also outlines the rules
def greating():
    print('\n\t'
          '*** Welcome to Crack the Passcode!!! ***\n\t'
          ' You will have 10 chances to crack the code.\n\t'
          ' The code length is 3 digits, and there will be no repeated numbers.\n\t'
          ' After submitting your answer, you will then receive a clue.\n\t'
          ' The clues are as follows.\n\t'
          ' A RED card means that all digits were incorrect.\n\t'
          ' A BLUE card means that one digit is correct but not in an incorrect position.\n\t'
          ' A GREEN card means that one digit is correct and is in the correct position.\n\t'
          ' Good LUCK!!!\n')

## time to generate a new passcode to be cracked
def mk_passcode(correct_string, correct_digits):
    number_pool = (range(0,10))
    correct_string = (random.sample(number_pool, 3)) 
    for digit in correct_string:
        correct_digits.append(int(digit))
    print(f'{correct_digits} <-correct_digits@mk_passcode()')
    
    return correct_digits

def get_guess(user_digits, user_string): #, user_ints):
    print('What do you think the passcode is?')
    user_string = (input('> '))
    for digit in user_string:
        user_digits.append(int(digit))

    return user_digits

def check_score(user_digits, correct_digits, cards):
    cycle = 0
    while cycle <= 2:
        for digit in user_digits:
            if digit not in correct_digits:
                cards.append('red.card')
                cycle += 1
            elif user_digits[int(cycle)] == correct_digits[int(cycle)]:
                cards.append('green.card')
                cycle += 1
            elif user_digits[int(cycle)] in correct_digits and user_digits[int(cycle)] != correct_digits[int(cycle)]:
                cards.append('blue.card')
                cycle += 1

    return cards


def show_score(cards, user_tries):
    num_cards = len(cards)
    display_cards = random.sample(cards, (num_cards))
    if cards.count('green.card') == 3:
        user_tries += 10
        print('Congrats!!! You CRACKED THE CODE!!!')
        return user_tries
    print(f'{display_cards} :Cards Displayed')


## simply calling the main function
main()
