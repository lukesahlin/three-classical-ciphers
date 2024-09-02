def CaeserEncryption(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    result = ""

    # For each char in the message check if the char exists in the alphabet
    # If it does then get the chars value (index) from the alphabet
    # Move the index by the key length and then mod by 27 
    # Add the new char to the result string 
    for char in message:
        if char in alphabet:
            originalChar = alphabet.index(char)
            newChar = (originalChar + alphabet.index(key) ) % 27
            result += alphabet[newChar]
        else:
            print("Invalid character!")
            break
    print (result)

def CaeserDecryption(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    result = ""

    # For each char in the message check if the char exists in the alphabet
    # If it does then get the chars value (index) from the alphabet
    # Move the index by the key length and then mod by 27 
    # Add the new char to the result string 
    for char in message:
        if char in alphabet:
            originalChar = alphabet.index(char)
            newChar = (originalChar - alphabet.index(key) ) % 27
            result += alphabet[newChar]
        else:
            print("Invalid character!")
            break
    print (result)




