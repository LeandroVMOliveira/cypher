# Data definition:

#  Command-line-argument is one of:

# - options    -- display the current ciphers and decipher available
# - check      -- try discover what type of the cipher is inputed
# - help       -- display the istruction to the user
#  intrep. utilize commands-line-arguments to return help, options or check function

# main.py -options return options()
# main.py -check return check()
# main.py -help return help()

# def fn_for_cla(option):
#return option()



# Key is Integer
# interp. shifts accord to alphabetic letters, that means key % possibilities

# keycheck(5) return 5     5 % 26
# keycheck(-1) return 25  -1 % 26
# keycheck(27) return 1    27 % 26


# cypher is Integer[1,9]
# interp. based on the options available to the user to choose with numbers

#- [1] cipher          when the user input the correct number
#- [2] decipher        an option is selected
#- [3] exit
# numcheck(1) return cipher()
# numcheck(2) return decipher()
# numcheck(3) return exit()

# def fn-for-cypher(n)
# return n function()


# templates:

import string

HEXDECIMAL = string.hexdigits + " "

DIGITS = string.digits + " "

BINARY = ["1", "0", " "]

MORSE = [".", "-", " "]

ALPHABETLOWER = string.ascii_lowercase
ALPHABETUPPER = string.ascii_uppercase
BASEALPHABET = ALPHABETLOWER + ALPHABETUPPER + " "
ALPHANUMERIC = ALPHABETLOWER + ALPHABETUPPER + DIGITS + " "


morse = {"A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..",
        "E" : ".", "F" : "..-.", "G" : "--.", "H" : "....",
        "I" : "..", "J" : ".---", "K" : "-.-", "L" : ".-..",
        "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.",
        "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-",
        "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-",
        "Y" : "-.--", "Z" : "--..", "0" : "-----", "1" : ".----",
        "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....",
        "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----."}
        

def fn_for_cipher():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to ... Cipher/Decipher!\
         \n\
         \n [1] cipher\
         \n [2] Decipher\
         \n [3] Exit\
         \n")
    mode = numcheck(1,3)
            
    if mode == 1:
        ...
    elif mode == 2:
        ...
    elif mode == 3:
        ...
    
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


def keycheck(keycap: int) -> int:
    while True:
        try:
            key = int(input("Insert the key number: "))
            if(key % keycap >= 0 and key % keycap <= 26):
                return key % keycap
        except ValueError:
            print("Insert a integer")


def inputcheck(checker, text: str) -> str:
    """Ensure that only specific input are used"""
    text = None
    while(True):
        test = True
        text = input("Insert the plaintext: ")
        for t in text:
            if not t in checker:
                test = False
        if(test):
            return text
        print(text)
        
def morseconv(plaintext: str) -> str:
    "converts alphanumeric into morse"
    result = ""
    for s in plaintext:
        if s.isalpha():
            result += morse[s.upper()] + " "
        elif s.isdigit:
            result += morse[s] + " "
        else:
            result += s
    return result

def morsedeconv(ciphertext:str) -> str:
    "converts morse into alphanumeric"
    result = ""
    data = []
    data = ciphertext.split(" ")
    
    for d in data:
        try:
            result += list(morse.keys())[list(morse.values()).index(d)]
        except(ValueError):
            print("invalid code")
            return result
    return result

def lencheck(error_mensage):
    "Ensures"
    while(True):
        test = True
        text = input("Insert the new alphabet(26 characters): ")
        if len(text) != 26:
            test = False
        if len(text) != len(set(text)):
            test = False
        if not text.isalpha():
            test = False
        if(test):
            text = text.lower()
            text += text.upper()
            text += " "
            return text
        print(error_mensage)
        
def lentest(keys:int, error_mensage):
    test = True
    text = input(f"Insert the keys({keys} characters): ")
    result = []
    if len(text) != keys:
        test = False
    if not text.isalpha():
        test = False
    print(text)
    if(test):
        for t in text:
            if t.isupper():
                result.append(ord(t) - ord("A") + 1)
            elif t.islower():
                result.append(ord(t) - ord("a") + 1)
        return result
    print(error_mensage)
    