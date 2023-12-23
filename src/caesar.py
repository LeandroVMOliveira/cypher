
from src import templates

def main() -> int:
    """Encoder/Decoder of Caesar cypher"""
    mode = None
    print("Welcome to Caesar Cypher/Decypher!\
         \nPlease select the method you want to choose:\
         \n\
         \n [1] Cypher\
         \n [2] Decypher\
         \n [3] Exit\
         \n")
    
    mode = templates.checknum(1,3)
    if mode == 1:
        cypher()
        return 0
    elif mode == 2:
        #decypher()
        return 0
    else:
        return 1
    
def cypher():
    key = None
    plaintext = None

    key = checkkey()
    plaintext = checktext()
    print (key, plaintext.isalpha)
def checkkey() -> int:
    while(True):
        try:
            key = int(input("Insert the key number: "))
            if(key % 26 >= 0 and key % 26 <= 26):
                return key % 26
        except(ValueError):
            print("Insert a integer")

def checktext() -> str:
    text = None
    while(True):
        text = input("Insert the plaintext: ")
        for t in text:
            if not t.isalpha:
                print("Only uses alphabetic letters")
                continue
        return text