from src import templates
import string

ALPHABETLOWER = string.ascii_lowercase
numbers = str(range(1,27))


def main():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to A1Z26 cipher/Decipher!\
         \nPlease select the method you want to choose:\
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
        text = input("Insert the plaintext: ")
        if not text.isdigit():
            test = False
        if(test):
            return text
        print("Insert only alphabetic letters")
    

def cipher(text):
    table = str.maketrans(ALPHABETLOWER, numbers)
    print(text.translate(table))
    return

def decipher(text):
    table = str.maketrans(numbers, ALPHABETLOWER)
    print(text.translate(table))
    return