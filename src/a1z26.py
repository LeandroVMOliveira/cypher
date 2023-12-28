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
    mode = numcheck(1,3)
    if mode == 1:
        text = textcheck()
        cipher(text)
    elif mode == 2:
        digits = digitcheck()
        decipher(digits)
    return 0

def numcheck(beg: int, end: int) -> int:
    """Ensures the correct number of answers"""
    while (True):
        try:
            mode = int(input("Please select the method you want to choose: "))
            if(mode >= beg and mode  <= end):
                return mode
            print("insert a valid choice")

        except(ValueError):
            print("insert a valid choice")

def textcheck() -> str:
    """Ensure tha only alphabetics letters are used"""
    text = None
    while(True):
        test = True
        text = input("Insert the plaintext: ")
        if not text.isalpha():
            test = False
        if(test):
            return text
        print("Insert only alphabetic letters")

def digitcheck() -> str:
    """Ensure tha only digits are used"""
    text = None
    while(True):
        test = True
        text = (input("Insert the ciphertext: "))
        if not text.isdigit():
            test = False
        if(test):
            return text
        print("Insert only digits")
    

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