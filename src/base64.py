from src import templates

import base64

def main():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to Base64 Cipher/Decipher!\
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
        return
    
    return 0

def cipher():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to ... Cipher/Decipher!\
         \n\
         \n [1] Base32\
         \n [2] Base64\
         \n [3] Base85\
         \n")
    mode = templates.numcheck(1,3)
            
    if mode == 1:
        text = templates.inputcheck(templates.BASEALPHABET)
        result = base64.b32encode(bytes(text, 'utf-8'))
        result_string = result.decode('utf-8')
        print(result_string)
        return
    elif mode == 2:
        text = templates.inputcheck(templates.BASEALPHABET)
        result = base64.b64encode(bytes(text, 'utf-8'))
        result_string = result.decode('utf-8')
        print(result_string)
        return
    elif mode == 3:
        text = templates.inputcheck(templates.BASEALPHABET)
        result = base64.b85encode(bytes(text, 'utf-8'))
        result_string = result.decode('utf-8')
        print(result_string)
        return
    
    return 0
    
def decipher():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to ... Cipher/Decipher!\
         \n\
         \n [1] Base32\
         \n [2] Base64\
         \n [3] Base85\
         \n")
    mode = templates.numcheck(1,3)
            
    if mode == 1:
        text = input("Insert the plaintext: ")
        result = base64.b32decode(bytes(text, 'utf-8'))
        result_string = result.decode('utf-8')
        print(result_string)
        return
    elif mode == 2:
        text = input("Insert the plaintext: ")
        result = base64.b64decode(bytes(text, 'utf-8'))
        result_string = result.decode('utf-8')
        print(result_string)
        return
    elif mode == 3:
        text = input("Insert the plaintext: ")
        result = base64.b85decode(bytes(text, 'utf-8'))
        result_string = result.decode('utf-8')
        print(result_string)
        return
    return 0