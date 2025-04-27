# martin burger
# burger_m@lynchburg.edu
# cs-131 final project
# v0.3 of game 2.3: Crack the Passcode

### ToDo
#   0.  Write up better comments
#   1.  Figure out a way to  prevent digits that earn a GREEN Card from
#           also earning a BLUE Card
#   2.  Wrap most of it up into a loop that
#           ends when user_digits == correct_digits is True
#           or 10 fatal attempts at guessing correct_digits
#   3.  [something I'm forgettings goes here]
        

# importing random.mod for use with passcode generation
import random

def main():
    greating()
    correct_string = str()
    correct_digits = list()
    mk_passcode(correct_string, correct_digits)
    print(f'{correct_digits} <- correct_digits@line.13.returned') #here for dev.testing
    user_digits = list()
    user_string = str()
    get_guess(user_digits, user_string)
    print(f'{user_digits} <- user_digits@line16.returned') #here for dev.testing
    cards = list()
    #user_ints = list()
    check_score(correct_digits, user_digits, cards)

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

def check_score(correct_digits, user_digits, cards):
    print(user_digits)
    if user_digits[0] == correct_digits[0]:
        cards.append('GREEN Card')
        if user_digits[1] == correct_digits[1]:
            cards.append('GREEN Card')
            if user_digits[2] == correct_digits[2]:
                cards.append('GREEN Card')
                print('Correct. You Win!')
        elif user_digits[2] == correct_digits[2]:
            cards.append('GREEN Card')
            blue_or_red(user_digits, correct_digits, cards)
        else:
            blue_or_red(user_digits, correct_digits, cards)
    elif user_digits[1] == correct_digits[1]:
        cards.append('GREEN card')
        if user_digits[2] == correct_digits[2]:
            cards.append('GREEN Card')
            blue_or_red(user_digits, correct_digits, cards)
        else:
            blue_or_red(user_digits, correct_digits, cards)
    elif user_digits[2] == correct_digits[2]:
        cards.append('GREEN Card')
        blue_or_red(user_digits, correct_digits, cards)
    else:
        blue_or_red(user_digits, correct_digits, cards)


# needs work -> this will generate a blue even if
# (digit) already got a GREEN Card
# I need to find a way to filter GREEN Card winning digits out
def blue_or_red(user_digits, correct_digits, cards):
    for digit in user_digits:
        if digit in correct_digits:
            cards.append('BLUE Card')
        elif digit not in correct_digits:
            cards.append('RED Card')
        
    print(f'{correct_digits} :Correct Code')
    print(f'{user_digits} :User Code')
    print(f'{cards} :Cards List')
    show_cards(cards)

def show_cards(cards):
    num_cards = len(cards)
    display_cards = random.sample(cards, (num_cards))
    print(f'{display_cards} :Cards Displayed')

## simply calling the main function
main()
