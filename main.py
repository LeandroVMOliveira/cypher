"""Module providing command-line-argument"""
import sys
from src import templates
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
    """Dysplay the ciphers"""


    print("""
[1] Caesar
[2] A1Z26
[3] Base64
[4] Binary
[5] Hexadecimal
[6] Morse
[7] Vigenère
[8] Substitution
""")
    mode = templates.numcheck(1,8)
    ciphers(mode)
    
def ciphers(n: int):
    """Receives a numbers and select a function placed in that number"""
    match n:
        case 1:
            requirements.caesar.main()
            return
        case 2:
            requirements.a1z26.main()
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
        case 6:
            requirements.hex.main()
            return
        case 7:
            requirements.hex.main()
            return
        case 8:
            requirements.hex.main()
            return
        
    return 0

def check():
    """Show all possibilities to decode"""
    print("Insert the code:")
    return


def hlp():
    """Manual of the code"""
    print("""
-options    -- Show all the ciphers available:
          
    Working:     
        Caesar
        A1Z26
        Base64 (32, 64, 85)
        Binary
        Hexadecimal
          
    On development:             
        Vigenère cipher
        Substitution cipher
        Morse
          
-check      -- make some steps to test if your code is one of the ciphers on the system

-help       -- open the help page
""")
    return


main()