from src import templates




def main():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to Hexadecimal Cipher/Decipher!\
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
    """Takes a data type option to convert to hexadecimal"""
    print("Select the data type\
         \n\
         \n [1] binary\
         \n [2] decimal\
         \n [3] exit\
         \n")
    data = templates.numcheck(1,4)
            
    if data == 1:
        hashdata = list()
        bina = templates.inputcheck(templates.BINARY)
        hashdata = bina.split(" ")
        for h in hashdata:
            print(hex(int(h, base=2))[2:])
        return
    elif data == 2:
        hashdata = list()
        number = templates.inputcheck(templates.DIGITS)
        hashdata = number.split(" ")
        for h in hashdata:
            print(hex(int(h, base=2))[2:])
        return
    else:
        return
def decipher():
    """Takes a hexadecimal to convert to a data type option """
    print("Select the data type\
         \n\
         \n [1] binary\
         \n [2] decimal\
         \n [3] exit\
         \n")
    data = templates.numcheck(1,4)
            
    if data == 1:
        hashdata = list()
        hexa = templates.inputcheck(templates.HEXDECIMAL)
        hexa = hexa.strip()
        hashdata = hexa.split(" ")
        for h in hashdata:
            h = int("0x" + h, base=16)
            print(bin(h)[2:], end=" ")
        return
    elif data == 2:
        hashdata = list()
        hexa = templates.inputcheck(templates.HEXDECIMAL)
        hexa = hexa.strip()
        hashdata = hexa.split(" ")
        for h in hashdata:
            h = int("0x" + h, base=16)
            print(h, end=" ")
        return
    else:
        return
    