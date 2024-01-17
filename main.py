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
            requirements.morse.main()
            return
        case 7:
            requirements.vigenere.main()
            return
        case 8:
            requirements.substitution.main()
            return
        
    return 0


def hlp():
    """Manual of the code"""
    print("""
-options    -- Show all the ciphers available:
          
    Working:
        Caesar(text, key)
          the code receives text (string) and a key and then it shifts 
          the alphabet according to the key. Example:

            text Good work

            key 1

            result Hppe xpsl
          
            text interesting

            key 15

            result xcitgthixcv
          
          text Good bye

            key -1

            result Fnnc axd
          
        A1Z26
        Base64 ()
        Binary
        Hexadecimal
          
    On development:             
        Vigenère cipher 2
        Substitution cipher 1
        Morse 3

-help       -- open the help page
""")
    return


main()