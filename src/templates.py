# Data definition:

#  Command-line-argument is one of:

# - options    -- display the current ciphers and decipher available
# - check      -- try discover what type of the cipher is inputed
# - help       -- display the istruction to the user
#  intrep. utilize commands-line-arguments to return help, options or check function

# main.py -options return options()
# main.py -check return check()
# main.py -help return help()


# Key is Integer
# interp. shifts accord to alphabetic letters, that means X % 26

# keycheck(5) return 5
# keycheck(-1) return 25
# keycheck(27) return 1


# mode is Integer[1,9]
# interp. based on the options available to the user to choose with numbers

#- [1] cipher          when the user input the correct number
#- [2] decipher        an option is selected
#- [3] exit
# numcheck(1) return cipher()
# numcheck(2) return decipher()
# numcheck(3) return exit()


# templates:

def fn_for_cipher():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to Caesar cipher/Decipher!\
         \nPlease select the method you want to choose:\
         \n\
         \n [1] cipher\
         \n [2] Decipher\
         \n [3] Exit\
         \n")
    numcheck(1,3)
            
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
            mode = int(input(" "))
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


def textcheck() -> str:
    text = None
    while(True):
        test = True
        text = input("Insert the plaintext: ")
        if not text.isalpha():
            test = False
        if(test):
            return text
        print("Insert only alphabetic letters")