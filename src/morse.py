from src import templates

def main():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to ... Cipher/Decipher!\
         \n\
         \n [1] cipher\
         \n [2] Decipher\
         \n [3] Exit\
         \n")
    mode = templates.numcheck(1,3)
            
    if mode == 1:
        plaintext = templates.inputcheck(templates.ALPHANUMERIC, "Insert alphanumeric characters only")
        print(templates.morseconv(plaintext))
    elif mode == 2:
        morse = templates.inputcheck(templates.MORSE, "Insert only morse caracters")
        print(templates.morsedeconv(morse))
    elif mode == 3:
        return
    
    return 0