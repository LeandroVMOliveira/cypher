
from requirements import templates

def main() -> int:
    """Encoder/Decoder of Caesar cypher"""
    mode = None
    print("Welcome to Caesar Cypher/Decypher!\
         \nPlease select the method you want to choose:\
         \n\
         \n [1] Cypher\
         \n [2] Decypher\
         \n [3] Exit\
         \n")
    
    mode = templates.checknum(1,3)
    if mode == 1:
        #cypher()
        return 0
    elif mode == 2:
        #decypher()
        return 0
    else:
        return 1