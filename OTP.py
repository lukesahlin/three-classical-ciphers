alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def EncryptOneTimePad(secret, key):
    secret = secret.upper()
    key = key.upper()

    if len(secret) != len(key):
        raise ValueError("secret and key are not the same length")

    encryptedSecret = ""
    for i in range(len(key)):
        secretIndex = alphabet.index(secret[i])
        keyIndex = alphabet.index(key[i])
        cipherVal = (secretIndex + keyIndex) % 27
        encryptedSecret += alphabet[cipherVal]

    return encryptedSecret

def DecryptOneTimePad(encryptedSecret, key):
    encryptedSecret = encryptedSecret.upper()
    key = key.upper()

    if len(encryptedSecret) != len(key):
        raise ValueError("secret and key are not the same length")

    secret = ""
    for i in range(len(key)):
        encryptedIndex = alphabet.index(encryptedSecret[i])
        keyIndex = alphabet.index(key[i])
        cipherVal = (encryptedIndex - keyIndex) % 27
        secret += alphabet[cipherVal]

    return secret



#test
plainText = "Hello friend"
key = "MONEYsasdfaa"
encryptedText = EncryptOneTimePad(plainText, key)
print("Cipher Text - " + encryptedText)
print("Message - " + DecryptOneTimePad(encryptedText, key))

