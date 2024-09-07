"""
This module provides functions to encrypt and decrypt messages using the One Time Pad (OTP) cipher.

Functions:
    encrypt_one_time_pad(secret, key):
        Encrypts a message using the OTP cipher.
    decrypt_one_time_pad(encrypted_secret, key):
        Decrypts a message encrypted with the OTP cipher.
"""



ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "


def encrypt_one_time_pad(secret, key):
    """ Encrypts a message using One Time Pad(OTP) cipher with the given key.
    Args:
        message (str): The plaintext message to be encrypted.
        key (str): A string of equal length that is the key for the cipher.

    Returns:
        str: The encrypted message.
    """
    secret = secret.upper()
    key = key.upper()

    if len(secret) != len(key):
        raise ValueError("secret and key are not the same length")

    encrypted_secret = ""
    for i, char in enumerate(secret):
        secret_index = ALPHABET.index(char)
        key_index = ALPHABET.index(key[i])
        cipher_val = (secret_index + key_index) % 27
        encrypted_secret += ALPHABET[cipher_val]

    return encrypted_secret


def decrypt_one_time_pad(encrypted_secret, key):
    """Decrypts a message encrypted with the One Time Pad(OTP) cipher using the given key.

    Args:
        message (str): The encrypted message to be decrypted.
        key (str): A string of equal length that was used as the key when the message was encrypted.

    Returns:
        str: The decrypted message.
    """
    encrypted_secret = encrypted_secret.upper()
    key = key.upper()

    if len(encrypted_secret) != len(key):
        raise ValueError("secret and key are not the same length")

    secret = ""
    for i, char in enumerate(encrypted_secret):
        encrypted_index = ALPHABET.index(char)
        key_index = ALPHABET.index(key[i])
        cipher_val = (encrypted_index - key_index) % 27
        secret += ALPHABET[cipher_val]

    return secret
