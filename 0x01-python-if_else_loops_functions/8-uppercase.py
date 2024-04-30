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
            # If the character is already uppercase or not a letter, append it to the result string
            uppercase_str += char

    # Print the entire uppercase string followed by a new line using string formatting
    print("{}".format(uppercase_str))
    print()  # Print an empty line
