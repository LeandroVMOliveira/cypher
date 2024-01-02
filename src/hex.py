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
    templates.numcheck(1,3)
            
    if mode == 1:
        cipher()
    elif mode == 2:
        ...
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
        text = templates.textcheck()
        return
    elif data == 2:
        number = templates.digitcheck()
        return
    elif data == 3:
        #templates.hexcheck()
        return
    else:
        return
    