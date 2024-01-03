from src import templates
import string

ALPHABETLOWER = string.ascii_lowercase
numbers = str(range(1,27))


def main():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to A1Z26 Cipher/Decipher!\
         \n\
         \n [1] cipher\
         \n [2] Decipher\
         \n [3] Exit\
         \n")
    mode = templates.numcheck(1,3)
    if mode == 1:
        text = templates.textcheck()
        cipher(text)
    elif mode == 2:
        digits = templates.digitcheck()
        decipher(digits)
    return 0


    

def cipher(text):
    for t in text:
        if t.islower():
            digit = ord(t )- ord("a") + 1
            if digit < 10:
                print(f"{digit:02d}", end="")
            else:
                print(digit, end="")
        elif t.isupper():
            digit = ord(t )- ord("A") + 1
            if digit < 10:
                print(f"{digit:02d}", end="")
            else:
                print(digit, end="")
        elif t.isdigit():
            print("", end="")
        else:
            print(t, end=" ")
    return

def decipher(text):
    hashdata = list()
    
    text = text.strip()
    hashdata = text.split(" ")
    for h in hashdata:
        for n, m in zip(h[0::2], h[1::2]) :
                
            total = int(n+m)+ ord("A") - 1
            print(chr(total), end="")
        print(" ", end="")
    return