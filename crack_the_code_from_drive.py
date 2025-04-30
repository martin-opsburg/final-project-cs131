import random

# this is the main function that outlines variables, lists,
# and fuctions used in the workflow

# this function is here for managing the user experience
# it tracks the number of tries the user has made,
# calls functions for getting the user's guesses, grading the guesses,
# and showing hints/cards
# it also clears values to reset them for the next prompt in the loop
def user_exp_loop():
    correct_string = str()
    correct_digits = list()
    mk_passcode(correct_string, correct_digits)
    user_tries = 0
    result=0
    user_digits = list()
    user_string = str()
    cards = list()
    result=0
    while user_tries <= 9:
        get_guess(user_digits, user_string)
        check_score(correct_digits, user_digits, cards, user_tries,result)
        show_score(cards, user_tries)
        user_string = ""
        if cards.count('green.card')==3:
            result=1
            break
        user_digits.clear()
        cards.clear()
        user_tries += 1
        #return result
   
    if user_tries == 10:
        print('Sorry, the code was not cracked.')
        print('Thanks for playing, nevertheless!')
        print('Exiting the game...')
        print()

    return result

## a simple welcome message
## that also outlines the rules
def greeting():
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

def get_guess(user_digits, user_string): 
    print('What do you think the passcode is?')
    user_string = (input('> '))
    for digit in user_string:
        user_digits.append(int(digit))
    
    return user_digits

def check_score(user_digits, correct_digits, cards, user_tries,result):
    cycle = 0
    while cycle <= 2:
        for digit in user_digits:
            if digit not in correct_digits:
                cards.append('red.card')
                cycle += 1
            elif user_digits[int(cycle)] == correct_digits[int(cycle)]:
                cards.append('green.card')
                cycle += 1
                #if int(cards.count('green.card')) == 3:
                    #win_exit()
            elif user_digits[int(cycle)] in correct_digits and user_digits[int(cycle)] != correct_digits[int(cycle)]:
                cards.append('blue.card')
                cycle += 1

    #return result

def show_score(cards, user_tries):
    print()
    num_cards = len(cards)
    display_cards = random.sample(cards, (num_cards))
    hint_card = ' : '.join(display_cards)
    print(f'{hint_card} :hint_card Displayed'
          '\n\t')

# a simple goodbye message
'''
def win_exit():
     print('Congrats, You CRACKED THE CODE!!!')
     print('Thanks for playing!')
     print('Exiting the game...')
     print()
'''

