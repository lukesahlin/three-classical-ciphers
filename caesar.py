def caesar_encryption(message, key):
    """Encrypts a message using Caesar cipher with the given key.

    Args:
        message (str): The plaintext message to be encrypted.
        key (str): A single character key for the Caesar cipher.

    Returns:
        str: The encrypted message.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    result = ""

    for char in message:
        if char in alphabet:
            original_char = alphabet.index(char)
            new_char = (original_char + alphabet.index(key)) % 27
            result += alphabet[new_char]
        else:
            print("Invalid character!")
            break

    print(result)
    return result


def caesar_decryption(message, key):
    """Decrypts a message encrypted with the Caesar cipher using the given key.

    Args:
        message (str): The encrypted message to be decrypted.
        key (str): A single character key used in the encryption.

    Returns:
        str: The decrypted message.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    result = ""

    for char in message:
        if char in alphabet:
            original_char = alphabet.index(char)
            new_char = (original_char - alphabet.index(key)) % 27
            result += alphabet[new_char]
        else:
            print("Invalid character!")
            break

    print(result)
    return result
