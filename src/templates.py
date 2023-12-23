# Data definition:

#  Command-line-argument is one of:
"""
 - options    -- display the current cyphers and decypher available
 - check      -- try discover what type of the cypher is inputed
 - help       -- display the istruction to the user
"""
#  intrep. utilize commands-line-arguments to return help, options or check function

# Key is Integer
# interp. shifts accord to alphabetic letters that means X % 26

# templates:

def fn_for_cypher():
    """Template for base code/decode method"""
    mode = None
    print("Welcome to Caesar Cypher/Decypher!\
         \nPlease select the method you want to choose:\
         \n\
         \n [1] Cypher\
         \n [2] Decypher\
         \n [3] Exit\
         \n")
    checknum(1,3)
            
    if mode == 1:
        ...
    elif mode == 2:
        ...
    elif mode == 3:
        ...
    
    return 0
    
def checknum(beg: int, end: int) -> int:
    """Ensures the correct number of answers"""
    while (True):
        try:
            mode = int(input(" "))
            if(mode >= beg and mode  <= end):
                return mode
            print("insert a valid choice")

        except(ValueError):
            print("insert a valid choice")



