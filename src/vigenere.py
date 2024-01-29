from src import templates
from . import caesar

def main():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to vigenere Cipher/Decipher!\
         \n\
         \n [1] cipher\
         \n [2] Decipher\
         \n [3] Exit\
         \n")
    mode = templates.numcheck(1,3)
            
    if mode == 1:
        plaintext = templates.inputcheck(templates.BASEALPHABET, "Insert alphabetic letters only")
        keys = templates.lentest(len(plaintext), "Invalid input")
        ciphertext = ""
        for i in range(len(plaintext)):
            ciphertext += caesar.cipher(keys[i],plaintext[i])
        print(ciphertext)
        
    elif mode == 2:
        ciphertext = templates.inputcheck(templates.BASEALPHABET, "Insert alphabetic letters only")
        keys = templates.lentest(len(ciphertext), "Invalid input")
        plaintext = ""
        for t, k in ciphertext, keys:
            plaintext += caesar.cipher(k,t)
        print(plaintext)
    elif mode == 3:
        return
    
    return 0