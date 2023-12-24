"""The base to form the cipher"""
import string

ALPHABETLOWER = string.ascii_lowercase
ALPHABETUPPER = string.ascii_uppercase

def main() -> int:
    """Encoder/Decoder of Caesar cipher"""
    mode = None
    print("Welcome to Caesar cipher/Decipher!\
         \nPlease select the method you want to choose:\
         \n\
         \n [1] cipher\
         \n [2] Decipher\
         \n [3] Exit\
         \n")
    
    mode = numcheck(1,3)
    if mode == 1:
        cipher()
        return 0
    elif mode == 2:
        #decipher()
        return 0
    else:
        return 1
    
def cipher():
    key = None
    plaintext = None

    key = keycheck(26)
    plaintext = textcheck()
    print (key, plaintext)


def numcheck(beg: int, end: int) -> int:
    """Ensures the correct number of answers"""
    while (True):
        try:
            mode = int(input(" "))
            if(mode >= beg and mode  <= end):
                return mode
            print("insert a valid choice")

        except(ValueError):
            print("insert a valid choice")

def keycheck(keycap: int) -> int:
    while(True):
        try:
            key = int(input("Insert the key number: "))
            if(key % keycap >= 0 and key % keycap <= 26):
                return key % keycap
        except(ValueError):
            print("Insert a integer")

def textcheck() -> str:
    text = None
    while(True):
        test = True
        text = input("Insert the plaintext: ")
        if not text.isalpha():
            test = False
        if(test):
            return text
        print("Insert only alphabetic letters")
