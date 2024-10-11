"""
This module provides methods to encrypt and decrypt messages using the Vigenere Cipher.
Also a method to create the key from a given keyword.

methods:
    create_key(message, keyword)
        creates the key used to encrypt/decrypt
    encrypt_vigenere(message, keyword)
        Encrypts a message using the Vigenere Cipher.
    decrypt_vigenere(message, keyword)
        Decrypts an encrypted Vigenere message.
"""

def create_key(message, keyword):
    """creates a key for the Vigenere Cipher to use for encrypting/decrypting

    Args:
        message (str): The plaintext message to be encrypted/decrypted.
        keyword (str): A single character/word/phrase to be used for encrypting/decrypting.

    Returns:
        str: The key.
    """

    key = list(keyword)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(message, keyword):
    """Encrypts a message using Vigenere Cipher with the given keyword.

    Args:
        message (str): The plaintext message to be encrypted.
        keyword (str): A single character/word/phrase to be used for encrypting/decrypting.

    Returns:
        str: The encrypted message.
    """
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    encrypted_message = []
    key = create_key(message, keyword)

    for i in range(len(message)):
        char_alphabet_index = alphabet.index(message[i])
        key_alphabet_index = alphabet.index(key[i])
        encrypted_char_index = (char_alphabet_index + key_alphabet_index) % 27
        print(message[i] + " ------> " + alphabet[encrypted_char_index])
        encrypted_message.append(alphabet[encrypted_char_index])
        
    return "".join(encrypted_message)

def decrypt_vigenere(message, keyword):
    """Decrypts a message using Vigenere Cipher with the given keyword.

    Args:
        message (str): The plaintext message to be encrypted.
        keyword (str): A single character/word/phrase to be used for encrypting/decrypting.

    Returns:
        str: The decrypted message.
    """
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    decrypted_message = []
    key = create_key(message, keyword)

    for i in range(len(message)):
        char_alphabet_index = alphabet.index(message[i])
        key_alphabet_index = alphabet.index(key[i])
        decrypted_char_index = (char_alphabet_index - key_alphabet_index) % 27
        print(message[i] + " ------> " + alphabet[decrypted_char_index])
        decrypted_message.append(alphabet[decrypted_char_index])
        
    return "".join(decrypted_message)