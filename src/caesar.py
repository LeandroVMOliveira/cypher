"""The base to form the cipher"""
import string

from src import templates


ALPHABETLOWER = string.ascii_lowercase
ALPHABETUPPER = string.ascii_uppercase

def main() -> int:
    """Encoder/Decoder of Caesar cipher"""
    mode = None
    print("Welcome to Caesar cipher/Decipher!\
         \n\
         \n [1] cipher\
         \n [2] Decipher\
         \n [3] Exit\
        \n")
    
    mode = templates.numcheck(1,3)
    key: int = None
    plaintext: str = None
    if mode == 1 or mode == 2:
        
        key = templates.keycheck(26)
        plaintext = templates.textcheck()

        if mode == 1:
            cipher(key, plaintext)
            return 0
        else:
            decipher(key, plaintext)
            return 0
    else:
        return 1
    
def cipher(key, text):
    alphabetshift = ALPHABETLOWER[key:] + ALPHABETLOWER[:key]
    table = str.maketrans(ALPHABETLOWER, alphabetshift)
    print(text.translate(table))
    return

def decipher(key, text):
    alphabetshift = ALPHABETLOWER[key:] + ALPHABETLOWER[:key]
    table = str.maketrans(alphabetshift, ALPHABETLOWER)
    print(text.translate(table))
    return