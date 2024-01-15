import string

from src import templates

ALPHABETUPPER = string.ascii_uppercase + " "

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
        a = range(1,27)
        for b in a:
            print(b, end="")
            print(",", end=" ")
        """cipheralphabet = input("insert 26 caracters: ") + " "
        if len(set(cipheralphabet)) == len(cipheralphabet):
            plaintext = templates.textcheck()
            table = str.maketrans(ALPHABETUPPER, cipheralphabet)
            print(f" {plaintext.translate(table)}")
        else:
            print("aaa")"""

    elif mode == 2:
        cipheralphabet = input("insert 26 caracters: ") + " "
        plaintext = templates.textcheck()
        table = str.maketrans(cipheralphabet, ALPHABETUPPER)
        print(f" {plaintext.translate(table)}")

    elif mode == 3:
        return
    
    return 0