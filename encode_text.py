# filename: encode_text
# author: Makenzie Brian
# description:

def shift_left(key, text):
    # loop through text increase letter ascii value or mass increase all?
    # lower case a-z is ASCII decimal 97-122
    # upper case A-Z is ASCII decimal 65-90
    for letter in text:
        print(letter, ord(letter))             # print original ACSII value
        # check if is within characters a-z and A-Z
        letter = letter + key

        print(letter, ord(letter))             # print new ACSII value
    return text_sl


def visual_cypher_encode():
    # print alphabet and cypher lined up
    print()