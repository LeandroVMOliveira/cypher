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
        ...
    elif mode == 3:
        ...
    
    return 0

def cipher():
    
    print("Select the data type\
         \n\
         \n [1] Text\
         \n [2] integers\
         \n [3] hex\
         \n [4] exit\
         \n")
    data = templates.numcheck(1,4)
            
    if data == 1:
        text = templates.textcheck()
        for t in text:
            t = int(ord(t))
            t = bin(t)
            t = int(t[2:])
            print(f"{t:08d}", end=" ")
        return
    elif data == 2:
        number = templates.digitcheck()
        number = int(number)
        number = bin(number)  
        number = int(number[2:])   
        print(f"{number:032d}")
        return
    elif data == 3:
        #templates.hexcheck()
        ...
    else:
        return