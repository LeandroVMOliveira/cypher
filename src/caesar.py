"""The base to form the cipher"""


from src import templates



def main() -> int:
    """Encoder/Decoder of Caesar cipher"""
    mode = None
    print("Welcome to Caesar Cipher/Decipher!\
         \n\
         \n [1] cipher\
         \n [2] Decipher\
         \n [3] All keys\
         \n [4] Exit\
        \n")
    
    mode = templates.numcheck(1,4)
    key: int = None
    plaintext: str = None
    if mode == 1 or mode == 2:
        
        key = templates.keycheck(26)
        plaintext = templates.inputcheck(templates.ALPHANUMERIC, "Insert alphanumeric characters only")

        if mode == 1:
            cipher(key, plaintext)
            return 0
        else:
            decipher(key, plaintext)
            return 0
    elif mode == 3:
        key = range(0,26)
        plaintext = templates.inputcheck(templates.ALPHANUMERIC, "Insert alphanumeric characters only")
        for k in key:
            cipher(k,plaintext)
        return 0
    else:
        return 1
    
def cipher(key, text):
    """Takes a key and a plaintext to generate the ciphertext"""
    alphabetshiftlower = templates.ALPHABETLOWER[key:] + templates.ALPHABETLOWER[:key]
    alphabetshiftupper = templates.ALPHABETUPPER[key:] + templates.ALPHABETUPPER[:key]
    alphabetshift = alphabetshiftlower + alphabetshiftupper + templates.DIGITS + " "
    basealphabet = templates.ALPHANUMERIC
    table = str.maketrans(basealphabet, alphabetshift)
    print(f"Key {key}: {text.translate(table)}")
    return

def decipher(key, text):
    """Takes a key and a ciphertext to generate the plaintext"""
    alphabetshiftlower = templates.ALPHABETLOWER[key:] + templates.ALPHABETLOWER[:key]
    alphabetshiftupper = templates.ALPHABETUPPER[key:] + templates.ALPHABETUPPER[:key]
    alphabetshift = alphabetshiftlower + alphabetshiftupper + " "
    basealphabet = templates.ALPHANUMERIC
    table = str.maketrans(alphabetshift, basealphabet)
    print(f"Key {key}: {text.translate(table)}")
    return