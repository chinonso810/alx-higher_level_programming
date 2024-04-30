#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for char in str:
        # Check if the character is lowercase
        if 'a' <= char <= 'z':
            # Convert the character to uppercase using ASCII manipulation
            uppercase_char = chr(ord(char) - 32)
            # Append the uppercase character to the result string
            uppercase_str += uppercase_char
        else:
            uppercase_str += char
    print("{}".format(uppercase_str))
