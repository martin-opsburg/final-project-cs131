# martin burger
# burger_m@lynchburg.edu
# cs-131 final project
# v0.3 of game 2.3: Crack the Passcode

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
    int_user = list()
    for digit in list_user:
        int_user.append(int(digit))
    check_score(int_user, list_user, list_passcode)

def check_score(int_user, list_user, list_passcode):
    print(int_user, list_passcode) # this print() is here for function testing
    cards = list()
    #if int_user == list_passcode: # this probably needs to be nested to get more than one Green Card
    #    print('Correct. You Win!')
    if int_user[0] == list_passcode[0]:
        print('Green Card')
        cards.append('GREEN Card')
        if int_user[1] == list_passcode[1]:
            print('Green Card')
            cards.append('GREEN Card')
            if int_user[2] == list_passcode[2]:
                print('Green Card')
                cards.append('GREEN Card')
                print(cards)
                print('Correct. You Win!')
        elif int_user[2] == list_passcode[2]:
            print('Green Card')
            cards.append('GREEN Card')
        else:
            blue_or_red(int_user, list_passcode, cards)
    elif int_user[1] == list_passcode[1]:
        print('Green Card')
        cards.append('GREEN card')
        if int_user[2] == list_passcode[2]:
            print('Green Card')
            cards.append('GREEN Card')
            blue_or_red(int_user, list_passcode, cards)
    elif int_user[2] == list_passcode[2]:
        print('Green Card')
        cards.append('GREEN Card')
        blue_or_red(int_user, list_passcode, cards)
    else:
        blue_or_red(int_user, list_passcode, cards)
    
    #show_cards(cards)

    #num_cards = len(cards)
    #show_cards = random.sample(cards, num_cards)
    #print(show_cards)

def blue_or_red(int_user, list_passcode, cards):
    cycles = 0
    for digit in int_user:
        if digit in list_passcode and digit != cards.index(cycles):
            print('Blue Card')
            cards.append('BLUE Card')
            cycles += 1
        elif digit not in list_passcode:
            print('Red Card')
            cards.append('RED Card')
            cycles += 1
        
    #return(cards)
    show_cards(cards)

def show_cards(cards):
    print(cards)
    num_cards = len(cards)
    display_cards = random.sample(cards, (num_cards))
    print(display_cards)


## simply calling the main function
main()


#def check_score(int_user, list_user, list_passcode):
#    if int_user == list_passcode:
#        print('Correct, you win!')
#    eliffor digit in list_user:
#        if digit not in list_user:
#            print('Red Card')

