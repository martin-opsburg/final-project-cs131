import random
def welcomeAskRandQuest():
    '''
    This function uses print statements to welcome the user to the Random Question
    '''
    print("Welcome to the Random Question Game")
    print("The first step of your adventure")
    print("You will be asked a randomly generated question")
    print("You only get one chance, so make it count")
    print("Good Luck!!!")
    print()
    
def Game1():
    '''
    input:none
    processing:store the dictionary with random questions and answers
               calls the askQuestion function to see if the answer is correct/incorrect
               uses an if statement to tell the user if the answer is correct/incorrect
               plays music based on correctness of the answer
    output:return 1 or 0 depending on the answer
    '''
    correctAnswerdict={'Square root of 225':'15','Capital of Montana':'Helena','Periodic element name for Gold':'Au','What year did World War I start':'1914','Currency of Japan':'Yen'}
    askQuest=askQuestion(correctAnswerdict)
    
    return askQuest

def askQuestion(dictionary):
    '''
    input: a dictionary
    processing:creates a list from the keys of the dictionary input
               creates a randomized list using the randint function from the random library
               prints the the question for the user to see
               asks for the user input to determine if the answer is correct
               uses an if statement to see if the dictionary is equal to the user response
    output: returns 1 if the userResponse is correct, 0 if incorrect
    '''
    keyList=list(dictionary.keys())
    randQuest=keyList[random.randint(0,len(keyList)-1)]
    print(randQuest,'?')
    userResponse=str(input("Enter your answer to the question "))
    capUserResponse=userResponse.capitalize()
    if dictionary[randQuest]==capUserResponse:
        return 1
    else:
        return 0
