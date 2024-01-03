"""The base to form the cipher"""
import string

from src import templates


ALPHABETLOWER = string.ascii_lowercase
ALPHABETUPPER = string.ascii_uppercase
DIGITS = string.digits

def main() -> int:
    """Encoder/Decoder of Caesar cipher"""
    mode = None
    print("Welcome to Caesar Cipher/Decipher!\
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
    """Takes a key and a plaintext to generate the ciphertext"""
    alphabetshiftlower = ALPHABETLOWER[key:] + ALPHABETLOWER[:key]
    alphabetshiftupper = ALPHABETUPPER[key:] + ALPHABETUPPER[:key]
    alphabetshift = alphabetshiftlower + alphabetshiftupper + DIGITS + " "
    basealphabet = ALPHABETLOWER + ALPHABETUPPER + DIGITS + " "
    table = str.maketrans(basealphabet, alphabetshift)
    print(text.translate(table))
    return

def decipher(key, text):
    """Takes a key and a ciphertext to generate the plaintext"""
    alphabetshiftlower = ALPHABETLOWER[key:] + ALPHABETLOWER[:key]
    alphabetshiftupper = ALPHABETUPPER[key:] + ALPHABETUPPER[:key]
    alphabetshift = alphabetshiftlower + alphabetshiftupper + " "
    basealphabet = ALPHABETLOWER + ALPHABETUPPER + " "
    table = str.maketrans(alphabetshift, basealphabet)
    print(text.translate(table))
    return