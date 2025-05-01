import random

# this is the main function that outlines variables, lists,
# and functions used in the workflow
# it also manages the user experience
# via a while-loop based on the number of code cracks attempted,
# calls functions for getting the user's guess, grading the guess,
# and showing hints/cards
# it also clears values to reset them for the next cycle of the loop
def user_exp_loop():
    correct_string = str()
    correct_digits = list()
    make_passcode(correct_string, correct_digits)
    user_tries = 0
    result=0
    user_digits = list()
    user_string = str()
    cards = list()
    result=0
    while user_tries <= 9:
        get_guess(user_digits, user_string)
        check_score(correct_digits, user_digits, cards, user_tries, result)
        show_score(cards)
        user_string = ""
        if cards.count('GREEN Card!')==3:
            result=1
            break
        user_digits.clear()
        cards.clear()
        user_tries += 1
   
    if user_tries == 10:
        print('Sorry, the code was not cracked.')
        print('Thanks for playing, nevertheless!')
        print('Goodbye.')
        print()

    return result

## a simple welcome message
## that also outlines the rules
def greeting():
    print('\n\t'
          '*** Welcome to Crack the Code!!! ***\n\t'
          ' You will have 10 chances to crack the code.\n\t'
          ' The code length is 3 digits, and there will be no repeated numbers.\n\t'
          ' After submitting your answer, your score will be returned as 3 cards.\n\t'
          ' The color of each card has meaning based on your answer.\n\t'
          ' ~~ Each RED Card! means a digit in your answer is not in the secret code.\n\t'
          ' ~~ Each BLUE Card! means a digit is in the secret code but in an incorrect position.\n\t'
          ' ~~ Each GREEN Card! means a digit is in the secret code and is in the correct position.\n\t'
          ' Get 3 GREEN Cards to WIN!!!\n\t'
          ' Good LUCK!!!\n')

# this is where a code is generated for each game
# first it creates a pool of numbers to draw from
# using the radom.mod 3 non-repeating are sampled from the pool
# they become the code the user must crack
# using a for-loop, the generated code is used to
# populate a list that will be used to check the user's score
def make_passcode(correct_string, correct_digits):
    number_pool = (range(0,10))
    correct_string = (random.sample(number_pool, 3)) 
    for digit in correct_string:
        correct_digits.append(int(digit))
    #print(f'{correct_digits} <-correct_digits@mk_passcode() here as dev feedback')
    
# this is for prompting the user for their code guess
# the user submission is then used to
# populate a list that will be used to check the user's score
def get_guess(user_digits, user_string): 
    print('What do you think the passcode is?')
    user_string = (input('> '))
    if len(user_string) != 3:
        print('*** Incorrect Number of Digits Entered ***\n\t'
              ' The secret code has three digits.\n\t'
              ' Please try again.')
        user_string = ""
        get_guess(user_digits, user_string)
    else:
        for digit in user_string:
            user_digits.append(int(digit))
    
# this functions grades the user's code submission
# since there the number of digits in the code is known (3)
# a while-loop is used to process the grading
# in serial each number of the user's submission is graded
# using if/elif statements within the while-loop
# the score of each digit is written to a list(cards)
def check_score(user_digits, correct_digits, cards, user_tries, result):
    cycle = 0
    while cycle <= 2:
        for digit in user_digits:
            if digit not in correct_digits:
                cards.append('RED Card!')
                cycle += 1
            elif user_digits[int(cycle)] == correct_digits[int(cycle)]:
                cards.append('GREEN Card!')
                cycle += 1
            elif user_digits[int(cycle)] in correct_digits and user_digits[int(cycle)] != correct_digits[int(cycle)]:
                cards.append('BLUE Card!')
                cycle += 1

# this is how the hints/cards are shown
# for an added challenge, the cards are shuffled
# if they were not shuffled
# the cards would align with the user's submitted numbers
# that would be too easy!
# the built-in len() function is used to determine
# how many cards to randomly sample/draw 'n show the user
# the .join is used to present the list in a
# more aesthetically please format
def show_score(cards):
    print()
    num_cards = len(cards)
    display_cards = random.sample(cards, (num_cards))
    hint_card = ' : '.join(display_cards)
    print(f'{hint_card} :hint_card Displayed'
          '\n\t')

