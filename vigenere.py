def vigenere_cipher(message, keyword, encrypt):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    if encrypt:
        return encrypt_vigenere(message, keyword, alphabet)
    else:
        return decrypt_vigenere(message, keyword, alphabet)


def create_key(message, keyword):
    key = list(keyword)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(message, keyword, alphabet):
    encrypted_message = []
    key = create_key(message, keyword)

    for i in range(len(message)):
        char_alphabet_index = alphabet.index(message[i])
        key_alphabet_index = alphabet.index(key[i])
        encrypted_char_index = (char_alphabet_index + key_alphabet_index) % 27
        print(message[i] + " ------> " + alphabet[encrypted_char_index])
        encrypted_message.append(alphabet[encrypted_char_index])
        
    return "".join(encrypted_message)

def decrypt_vigenere(message, keyword, alphabet):
    decrypted_message = []
    key = create_key(message, keyword)

    for i in range(len(message)):
        char_alphabet_index = alphabet.index(message[i])
        key_alphabet_index = alphabet.index(key[i])
        decrypted_char_index = (char_alphabet_index - key_alphabet_index) % 27
        print(message[i] + " ------> " + alphabet[decrypted_char_index])
        decrypted_message.append(alphabet[decrypted_char_index])
        
    return "".join(decrypted_message)