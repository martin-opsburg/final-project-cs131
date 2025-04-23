import random as rr
def main():
    askRandQuest()
    

def askRandQuest():
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
    if askQuest==1:
        print("Your answer is correct!!!") # then can also have the music for correct
    else:
        print("Your answer is wrong. Better luck next time.") #then can enter loser music
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
    randQuest=keyList[rr.randint(0,len(keyList)-1)]
    print(randQuest,'?')
    userResponse=str(input("Enter your answer to the question "))
    capUserResponse=userResponse.capitalize()
    if dictionary[randQuest]==capUserResponse:
        return 1
    else:
        return 0

main()
