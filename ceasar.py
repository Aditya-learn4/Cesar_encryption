
text = 'Hello Zaira'
shift = 3

def ceasar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in message.lower():
        if char == ' ':
            encrypted_text += char
            #print(encrypted_text)
        else:
            index = alphabet.find(char)
            #print(index)
            new_index = (index + offset) % len(alphabet)
            #print(new_index)
            encrypted_text += alphabet[new_index]
    print('Plain text:', message) 
    print('encrypted text:', encrypted_text)
ceasar('Big Bang Theory', 5)