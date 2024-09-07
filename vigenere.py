def VigenereCipher(message, keyword, encrypt):
    if encrypt:
        VigenereCipherEncrypt(message, keyword)
    else:
        VigenereCipherDecrypt(message, keyword)


def VigenereCipherEncrypt(message, keyword):
    # check if keyword is smaller than message
    if len(keyword) < len(message):
        # make keyword into key
        for i in len(message):
            keyword 
        for char in message:
            pass
