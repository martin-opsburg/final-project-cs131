import random

def message():
    print("Welcome to Game 2! \n\t"
          '* For this game, you will be given a random 5 character sequence. \n\t'
          '* This sequence has actually been encoded.\n\t'
          '* You must decipher it with another 5 character sequence. \n\t'
          '* Guess the correct sequence to win and progress on your journey. \n')
            

def keyEncryption():  # Collects and compares the encrypted sequence and the user's answer
    
    rand_seq = generateRandSeq(5)

    encryp_seq = getEncrypted(rand_seq)
    printEncryp = ''.join(encryp_seq)
    
    print("Can you decode this sequence?",printEncryp)
    user_input = input().upper()
    user_seq=list(user_input)

    user_encryp = getEncrypted(user_seq)
    if user_encryp == encryp_seq:
        result = 1
    else:
        result = 0

    return result

def generateRandSeq(n): # Generates a random sequence of characters (length = n)
    encrypDico = generateEncDico()
    keys = list(encrypDico.keys())
    
    rand_seq = list()
    
    for nb in range(1,n+1):
        while True:
            ele = keys[random.randint(0,25)]
            
            if ele in rand_seq:
                pass
            else:
                rand_seq.append(ele)
                break
            
    return rand_seq

def generateEncDico():  # Generates a dictionary used for encryption
    encrypDico = {'A':'Z', 'B':'Y', 'C':'X', 'D':'W', 'E':'V', 'F':'U', 'G':'T',
                  'H':'S', 'I':'R', 'J':'Q', 'K':'P', 'L':'O', 'M':'N', 'N':'M',
                  'O':'L', 'P':'K', 'Q':'J', 'R':'I', 'S':'H', 'T':'G', 'U':'F',
                  'V':'E', 'W':'D', 'X':'C', 'Y':'B', 'Z':'A'}
    return encrypDico

def getEncrypted(seq):  # Uses dictionary to encrypt the input sequence
    encrpyDico = generateEncDico()

    encryp_seq = list()
    for ele in seq:
        encryp_seq.append(encrpyDico[ele])
    return encryp_seq



