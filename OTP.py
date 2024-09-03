def EncryptOneTimePad(secret, key):
    secret = secret.upper()
    key = key.upper()

    if len(secret) != len(key):
        raise ValueError("secret and key are not the same length")
    
    encryptedSecret = ""
    for i in range(len(key)):
        cipher_val = (ord(secret[i]) - ord('A') + ord(key[i]) - ord('A')) % 26
        encryptedSecret += chr(cipher_val + ord('A'))

    return encryptedSecret
def DecryptOneTimePad(encryptedSecret, key):
    encryptedSecret = encryptedSecret.upper()
    key = key.upper()

    if len(encryptedSecret) != len(key):
        raise ValueError("secret and key are not the same length")

    secret = ""
    for i in range(len(key)):
        cipher_val = (ord(encryptedSecret[i]) - ord('A') - (ord(key[i]) - ord('A'))) % 26
        secret += chr(cipher_val + ord('A'))

    return secret


#test
plainText = "Hello "
key = "MONEYs"
encryptedText = EncryptOneTimePad(plainText, key)
print("Cipher Text - " + encryptedText)
print("Message - " + DecryptOneTimePad(encryptedText, key))

