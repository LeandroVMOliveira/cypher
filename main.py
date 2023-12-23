"""Module prividing command-line-argument"""
import sys

import requirements

def main():
    """ensure the correct number of arguments"""
    if len(sys.argv) !=2:
        return sys.exit("utilize python main.py -help to learn about the script")      

    if sys.argv[1] == "-options":
        options()
    elif sys.argv[1] == "-check":
        check()
    elif sys.argv[1] == "-help":
        hlp()
    else:
        return sys.exit("utilize python main.py -help to learn about the script")
    return 0

def options():
    """Dysplay the cyphers"""


    print("[1] Caesar\
         \n[2] AZ26\
         \n[3] Base64\
         \n[4] Binary\
         \n[5] Hexadecimal")
    mode = numcheck(1,5)
    cyphers(mode)
    
def cyphers(n):
    match n:
        case 1: 
            requirements.caesar.main()
            return
        case 2:
            requirements.az26.main()
            return
        case 3:
            requirements.base64.main()
            return
        case 4:
            requirements.binary.main()
            return
        case 5:
            requirements.hex.main()
            return

def check():
    print("Insert the code:")
    return


def hlp():
    """Manual of the code"""
    print( "-options    -- Discover all the cyphers available\
          \n-check      -- make some steps to test if your code is one of the cyphers on the system\
          \n-help       -- open the help page")
    return

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



main()