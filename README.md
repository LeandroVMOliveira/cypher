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
          
          text Good bye

            key -1

            result Fnnc axd
          
        A1Z26(text)
          Recive text(string) and replace letters to numbers based on their place index. Example:

          text    I love you

          result  09 12152205 251521

        Base64(ascii letters)
          receive an input(everything on ascii table) and makes some kind of conversion,
          first the string is converted to binary where every character is 8 bits or one byte

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

        Binary
        Hexadecimal
          
    On development:             
        Vigenère cipher 2
        Substitution cipher 1
        Morse 3
