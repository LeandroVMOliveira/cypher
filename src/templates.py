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

ALPHABETLOWER = string.ascii_lowercase
ALPHABETUPPER = string.ascii_uppercase
BASEALPHABET = ALPHABETLOWER + ALPHABETUPPER + " "
ALPHANUMERIC = ALPHABETLOWER + ALPHABETUPPER + DIGITS + " "

A1Z26 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"
        , "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"
        , "21", "22", "23", "24", "25", "26"]

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


def inputcheck(checker) -> str:
    """Ensure tha only alphabetics letters are used"""
    text = None
    while(True):
        test = True
        text = input("Insert the plaintext: ")
        for t in text:
            if not t in checker:
                test = False
        if(test):
            return text
        print("Insert only alphabetic letters")