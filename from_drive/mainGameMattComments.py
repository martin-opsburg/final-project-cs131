import beginningMusic as beginMus
import SoundCode
import crack_the_code as Game3
import askRandQuestFinal as Game1
import cs_finalGame2Finished as Game2


def main():
    mainGame()
      
def mainGame():
    '''
    input:none
    processing: asks for the user's name and if they want to play the game
                plays a beginning music file of waves by importing the beginningMusic file
                which plays a wav file for 6 seconds using the time library
                calls functions of the games and uses nested if statements
                if the answers are correct
                calls the function playSound() that plays sound based of incorrect/correct answer
    '''
    name=input("What is your name? ")
    print("Hello"," ",name,'!', sep="",end=" ")
    print("Are you ready for an adventure?")
    while True:
        userPlay=int(input("Type 1 to play or -99 to stop "))
        
        successSteps=0

        if userPlay==1:
            beginMus.beginMusic()
            drawBoard(successSteps)
            print()
            Game1.welcomeAskRandQuest()
            RandQuestGame=Game1.Game1()
            SoundCode.playSound(RandQuestGame)
            if RandQuestGame==1:
                print()
                print("Your answer is correct!!")
                print("Congratulations!! You passed the first game!!")
                print()
                successSteps+=1
                drawBoard(successSteps)
                print()
                Game2.message()
                KeyEncryp=Game2.keyEncryption()
                SoundCode.playSound(KeyEncryp)
                if KeyEncryp==1:
                    print()
                    print("Your answer is correct!!")
                    print("Congratulations!! You passed the second game!!")
                    print()
                    successSteps+=1
                    drawBoard(successSteps)
                    Game3.greeting()
                    CrackCode=Game3.user_exp_loop()
                    SoundCode.playSound(CrackCode)
                    
                    if CrackCode==1:
                        print("You cracked the code!!")
                        print("Congratulations!! You won the game!!")
                        print()
                    
                    elif CrackCode==0:
                        print("Sorry, the code was not cracked")
                        print("You lost the game. Better luck next time!")
                        
                elif KeyEncryp==0:
                    print("You failed to enter the correct unenrypted version of the encrypted sequence")
                    print("Thank you for playing the game. Better luck next time!")
                    
            elif RandQuestGame==0:
                print("You failed to give the correct answer for the question")
                print("Thank you for playing the game. Better luck next time!")
                
        elif userPlay==-99:
            print("Exiting the Game")
            break
        else:
            print("Error. You entered an invalid number. Try again!!")
        
def drawBoard(successful_steps):
    '''
    input:takes takes the number of successful steps
    processing: creates the list with the game locations
                uses a for loop to print <You are here> based on the succesful steps
    output:none
    '''
    boardList=["Random Question ~~~~~~~~~~~~~~~~~~~~~","Key Encription  ~~~~~~~~~~~~~~~~~~~~~","Cracking the Passcode ~~~~~~~~~~~~~~~"]
    print("--------------Game Status--------------")
    for pos in range(len(boardList)):
        if pos==successful_steps:
            print("<You are here>")
        print(boardList[pos])
    print("---------------------------------------")


main()
