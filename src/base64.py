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
    text = templates.textcheck()
    result = base64.b64encode(bytes(text, 'utf-8'))
    result_string = result.decode('utf-8')
    print(result_string)
    return
def decipher():
    text = input()
    result = base64.b64decode(bytes(text, 'utf-8'))
    result_string = result.decode('utf-8')
    print(result_string)
    return