
import string
from src import templates






def main():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to binary Cipher/Decipher!\
         \n\
         \n [1] cipher\
         \n [2] Decipher\
         \n [3] Exit\
         \n")
    mode = templates.numcheck(1,3)
            
    if mode == 1:
        cipher()
    elif mode == 2:
        decipher()
    elif mode == 3:
        ...
    
    return 0

def cipher():
    """Takes a data type option to convert to binary"""
    print("Select the data type\
         \n\
         \n [1] Text\
         \n [2] Decimal\
         \n [3] hex\
         \n [4] exit\
         \n")
    data = templates.numcheck(1,4)
            
    if data == 1:
        text = templates.inputcheck(templates.BASEALPHABET)
        for t in text:
            t = int(ord(t))
            t = bin(t)[2:]
            t = int(t)
            print(f"{t:08d}", end=" ")
        print()
        return
    elif data == 2:
        number = templates.inputcheck(templates.DIGITS)
        number = int(number)
        number = bin(number)[2:]
        number = int(number)
        print(f"{number:04d}")
        
        return
    elif data == 3:
        hashdata = list()
        hexa = templates.inputcheck(templates.HEXDECIMAL)
        hexa = hexa.strip()
        hashdata = hexa.split(" ")
        for h in hashdata:
            h = int("0x" + h, base=2)
            print(bin(h)[2:], end=" ")
        return
    else:
        return
    

def decipher():
    """Takes a binary to convert to a data type option"""
    print("Select the data type\
         \n\
         \n [1] Text\
         \n [2] Decimal\
         \n [3] hex\
         \n [4] exit\
         \n")
    data = templates.numcheck(1,4)
            
    if data == 1:
        hashdata = list()
        text = templates.inputcheck(templates.BINARY)
        text = text.strip()
        hashdata = text.split(" ")
        for h in hashdata:
            print(chr(int(h, 2)), end="")
        print() 
        return
    elif data == 2:
        hashdata = list()
        text = templates.inputcheck(templates.BINARY)
        text = text.strip()
        hashdata = text.split(" ")
        for h in hashdata:
            print(int(h, 2), end="")
        print()
        return
    elif data == 3:
        bina = templates.inputcheck(templates.BINARY)
        bina = int(bina, base=2)
        print(hex(bina)[2:])
        return
    else:
        return