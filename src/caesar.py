
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
        #cypher()
        return 0
    elif mode == 2:
        #decypher()
        return 0
    else:
        return 1
    
def cypher():
    key: int = None
    plaintext: str = None
    key = int(input("Insert the key number: "))
    plaintext = input("Inserte the plaintext: ")
    if(checktext(key,plaintext)):
        print("Insert the correct type values")
        cypher()

def checktext(key, text) -> bool:
    if not key.isdigit or key == 0:
        return True
    if not text.isalpha:
        return True
    return False