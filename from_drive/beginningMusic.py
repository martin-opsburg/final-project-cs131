import winsound
import time

def beginMusic():
    '''
    input:none
    processing: uses the winsound and time libraries
                plays the begin_music file
                uses time.sleep(6) to play that file for 6 seconds
                then plays nothing
    output:none
    '''
    begin_music="lake-waves-lapping-on-the-beach-01.wav"
    winsound.PlaySound(begin_music,winsound.SND_ASYNC | winsound.SND_FILENAME)
    time.sleep(6)
    winsound.PlaySound(None,winsound.SND_ASYNC | winsound.SND_FILENAME)


