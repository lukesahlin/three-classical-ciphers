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
        char_alhpabet_index = alphabet.index(message[i])
        key_alphabet_index = alphabet.index(key[i])
        encrypted_char = alphabet[(char_alhpabet_index + key_alphabet_index) % 27]
        encrypted_message.append(encrypted_char)
        
    return "".join(encrypted_message)

def decrypt_vigenere(message, keyword, alphabet):
    decrypted_message = []
    key = create_key(message, keyword)

    for i in range(len(message)):
        char_alhpabet_index = alphabet.index(message[i])
        key_alphabet_index = alphabet.index(key[i])
        decrypted_char = alphabet[(char_alhpabet_index - key_alphabet_index) % 27]
        decrypted_message.append(decrypted_char)
        
    return "".join(decrypted_message)