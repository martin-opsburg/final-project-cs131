
from random import randint

def game2():
    result = keyEncryption()

    print(result)

def keyEncryption():
    
    rand_seq = generateRandSeq(5)
    #encrpyDico = generateEncDico()

    encryp_seq = getEncrypted(rand_seq)
    
    print("Cen you decode this sequence? ", encryp_seq)
    #user_seq = list(input())
    #user_seq.upper()
    user_input = input().upper()
    user_seq=list(user_input)

    user_encryp = getEncrypted(user_seq)
    if user_encryp == encryp_seq:
        result = 1
    else:
        result = 0

    return result

def generateRandSeq(n):
    encrypDico = generateEncDico()
    keys = list(encrypDico.keys())
    
    rand_seq = list()
    
    for nb in range(1,n+1):
        while True:
            ele = keys[randint(0,25)]
            
            if ele in rand_seq:
                pass
            else:
                rand_seq.append(ele)
                break
            
    return rand_seq

def generateEncDico():
    encrypDico = {'A':'Z', 'B':'Y', 'C':'X', 'D':'W', 'E':'V', 'F':'U', 'G':'T',
                  'H':'S', 'I':'R', 'J':'Q', 'K':'P', 'L':'O', 'M':'N', 'N':'M',
                  'O':'L', 'P':'K', 'Q':'J', 'R':'I', 'S':'H', 'T':'G', 'U':'F',
                  'V':'E', 'W':'D', 'X':'C', 'Y':'B', 'Z':'A'}
    return encrypDico

def getEncrypted(seq):
    encrpyDico = generateEncDico()

    encryp_seq = list()
    for ele in seq:
        encryp_seq.append(encrpyDico[ele])
    return encryp_seq

game2()
