import winsound

def playSound(returnOfGame):
    '''
    input:return from the other games
    processing: if statement the plays a winning sound if returnOfGame=1 and losing sound if returnOfGame=0
    output:none
    '''
    file1="beep-05.wav"
    file2="applause-3.wav"
    if returnOfGame==0:
        winsound.PlaySound(file1,winsound.SND_ASYNC | winsound.SND_FILENAME)
    elif returnOfGame==1:
        winsound.PlaySound(file2,winsound.SND_ASYNC | winsound.SND_FILENAME)
    
