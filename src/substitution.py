
from src import templates



def main():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to ... Cipher/Decipher!\
         \n\
         \n [1] cipher\
         \n [2] Decipher\
         \n [3] Exit\
         \n")
    mode = templates.numcheck(1,3)
            
    if mode == 1:
        
        cipheralphabet = input("insert 26 caracters: ") + " "
        
        if len(set(cipheralphabet)) == len(cipheralphabet):
            plaintext = templates.inputcheck(templates.BASEALPHABET, "Insert alphabetic letters only")
            table = str.maketrans(templates.ALPHABETUPPER + " ", cipheralphabet)
            print(f" {plaintext.translate(table)}")
        else:
            print("aaa")

    elif mode == 2:
        cipheralphabet = input("insert 26 caracters: ") + " "
        plaintext = templates.inputcheck(templates.BASEALPHABET, "Insert alphabetic letters only")
        table = str.maketrans(cipheralphabet, templates.ALPHABETUPPER + " ")
        print(f" {plaintext.translate(table)}")

    elif mode == 3:
        return
    
    return 0