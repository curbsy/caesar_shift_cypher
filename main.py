# filename: main
# author: Makenzie Brian
# description:

import encode_text
import decode_text

def main():
    # take filename OR text and key as user input
    # check key is whole number and filename is valid
    """
    while True:
        try:
            user_command = input("Encode(e) or decode(d)?")
        except ValueError:     # typeerror?
            print("Please enter a valid option")
            continue
        else:
            break
    """


    user_command = input("Encode(e) or decode(d)?")
    user_text = input("Input text:")
    user_key = input("Key?")



