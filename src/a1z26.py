from src import templates
import string

ALPHABETLOWER = string.ascii_lowercase
numbers = str(range(1,27))


def main():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to A1Z26 cipher/Decipher!\
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
        digit = ord(t )- ord("a") + 1
        if digit < 10:
            print(f"{digit:02d}", end="")
        else:
            print(digit, end="")
    return

def decipher(text):
    for n, m in zip(text[0::2], text[1::2]) :
        
        total = int(n+m)+ ord("a") - 1
        print(chr(total), end="")
    return