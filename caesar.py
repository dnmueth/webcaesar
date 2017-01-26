def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in range(len(alphabet)):
        if alphabet[char].upper() == letter:
            return char
        elif alphabet[char] == letter:
            return char

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if rot <= 25 and char.isalpha():
        newchar = int((alphabet_position(char) + rot) % 26)
        if char.isupper():
            return alphabet[newchar].upper()
        return alphabet[newchar]
    elif rot>25 and char.isalpha():
        newchar = int((alphabet_position(char) + rot) % 26)
        newchar = newchar % 25
        if char.isupper():
            return alphabet[newchar].upper()
        return alphabet[newchar]
    else:
        return char
        
def encrypt(text, rot):
    newtext = ''
    for x in text:
        newtext = newtext + rotate_character(x,rot)
    return newtext