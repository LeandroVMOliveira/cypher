<h1>Cypher</h1>

Working:

Caesar(text, key)       
    the code receives text (string) and a key and then it shifts 
    the alphabet according to the key. Example:
    
    text Good work
    key 1
    
    result Hppe xpsl
                
    text interesting
    key 15
    
    result xcitgthixcv
          
    text Goodbye
    key -1
    
    result Fnncaxd
          
A1Z26(text)

Receive text(string) and replace letters with numbers based on their place index. Example:

    text    I love you
    
    result  09 12152205 251521

Base64(ASCII letters)
    receive an input(everything on ASCII table) and makes some kind of conversion,
    first, the string is converted to binary where every character is 8 bits or one byte

          01000010 01111001 01100101
              B        y       e
          
then the binary string is splited 3 bytes each just like the example above, and anothe
spit it's made for each 6 bits
 
          010000 100111 100101 100101
             Q     n      l      l
          
and the 4 binary sets are converted to numbers that are indexes on Base64 "alphabet" that go
from a to z lower and upper, 0 to 9, "+" and "/"

          010010 000110 1001  None
             S     G      k     =
          
when 3 bytes can't be formed a equal sign "=" is put in place.

Binary(text or numbers or hexadecimal)

takes an input and convert to binary or make it backwards according with ASCII table 
in case if are text, and making normal conversion case are other numeric based system.

Example:

    input Stereo
    result 01010011 01110100 01100101 01110010 01100101 01101111
               S        t        e        r        e       o
    ASCII     83       116      101      114      101     111
          
      input    50
      result 110010

      input        f7a
      result   111101111010

Hexadecimal(binary or integer)
      convert hexadecimal to binary integers
      Example:

        input   75  (base 10)
        result  4b  (base 16)
          
        input   1000101 (base 2)
        result     45   (base 16)
                  
Vigenère cipher (keys: str, plaintext: str)
    takes two strings one is the plaintext and the other is the key to make the shift on the characters
    Example:

            input  Hello (plaintext)
                   Spear (keys)
First, the keys are converted to numbers as we used on A1Z26

            S  p  e  a  r
            19 16 05 01 18
So, we shift the corresponding letter by the key

              Z       t        p       l       f
            H + 19  e + 16   l + 05  l + 01  o + 18

            result Auqmg
            
        Substitution cipher 
        Morse 
