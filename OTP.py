alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "


def encrypt_one_time_pad(secret, key):
    secret = secret.upper()
    key = key.upper()

    if len(secret) != len(key):
        raise ValueError("secret and key are not the same length")

    encrypted_secret = ""
    for i in range(len(key)):
        secret_index = alphabet.index(secret[i])
        key_index = alphabet.index(key[i])
        cipher_val = (secret_index + key_index) % 27
        encrypted_secret += alphabet[cipher_val]

    return encrypted_secret


def decrypt_one_time_pad(encrypted_secret, key):
    encrypted_secret = encrypted_secret.upper()
    key = key.upper()

    if len(encrypted_secret) != len(key):
        raise ValueError("secret and key are not the same length")

    secret = ""
    for i in range(len(key)):
        encrypted_index = alphabet.index(encrypted_secret[i])
        key_index = alphabet.index(key[i])
        cipher_val = (encrypted_index - key_index) % 27
        secret += alphabet[cipher_val]

    return secret
