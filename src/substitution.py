
from src import templates



def main():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to substitution Cipher/Decipher!\
         \n\
         \n [1] cipher\
         \n [2] Decipher\
         \n [3] Exit\
         \n")
    mode = templates.numcheck(1,3)
            
    if mode == 1:
        
        cipheralphabet = templates.lencheck("Incorrect usage")
        
        plaintext = templates.inputcheck(templates.BASEALPHABET, "Insert alphabetic letters only")
        table = str.maketrans(templates.BASEALPHABET, cipheralphabet)
        print(f" {plaintext.translate(table)}")
        
    elif mode == 2:
        cipheralphabet = templates.lencheck("Incorrect usage")
        plaintext = templates.inputcheck(templates.BASEALPHABET, "Insert alphabetic letters only")
        table = str.maketrans(cipheralphabet, templates.BASEALPHABET)
        print(f" {plaintext.translate(table)}")

    elif mode == 3:
        return
    
    return 0