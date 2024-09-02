from Caeser import *
from OTP import *
def option_ceasar_cipher():
    # running ceasar cipher
    print("Running ceasar cipher")
    message = input("Enter the message to encrypt/decrypt: ")
    action = input("Do you want to (e)ncrypt or (d)ecrypt: ").lower()
    key = input("Enter the key for encryption/decryption (a letter): ")

    if action == 'e':
        print("Encrypting message in Ceasar Cipher")
        CaeserEncryption(message.upper(), key.upper())
        return
    if action == 'd':
        print("Decrypting message in Ceasar Cipher")
        CaeserDecryption(message.upper(), key.upper())
        return
    else:
        print("Not a valid selection, please choose 'e' for encrypt and 'd' for decrypt.")
        option_ceasar_cipher() # recursively call function to go back again


def option_vigenere_cipher():
    # running the vigenere cipher
    print("Running vigenere cipher")
    message = input("Enter the message to encrypt/decrypt: ")
    action = input("Do you want to (e)ncrypt or (d)ecrypt: ").lower()
    key = input("Enter the key for encryption/decryption (a word): ")

    if action == 'e':
        print("Encrypting message in Vigenere Cipher")
        # logic here for vigenere encryption
        return # exit the function after success (may not be needed after integrating functions)
    if action == 'd':
        print("Decrypting message in Vigenere Cipher")
        # logic here for vigenere decryption
        return # exit the function after success (may not be needed after integrating functions)
    else:
        print("Not a valid selection, please choose 'e' for encrypt and 'd' for decrypt")
        option_vigenere_cipher() # recursively call function to go back again

def option_otp_cipher():
    # run the otp cipher
    print("Running otp cipher")
    message = input("Enter the message to encrypt/decrypt: ")
    action = input("Do you want to (e)ncrypt or (d)ecrypt: ").lower()
    key = input("Enter the key for encryption/decryption (must be as long as the message): ")

    # check if the key is equally as long as the message
    if len(key) != len(message):
        print("Key must be the same length as the message")
        option_otp_cipher()
        return

    if action == 'e':
        hiddenMessage = EncryptOneTimePad(message, key)
        print("Encrypting message in OTP Cipher")
        print("your secret message is " + hiddenMessage)
        return
    if action == 'd':
        secret = DecryptOneTimePad(message, key)
        print("Decrypting message in OTP Cipher")
        print("your secret is " + secret)
        return 
    else:
        print("Not a valid selection, please choose 'e' for encrypt and 'd' for decrypt")
        option_otp_cipher() # recursively call function to go back again


def main():
    # test
    print("Choose an option of what cipher to use:")
    print("1. Choose Ceaser Cipher")
    print("2. Choose Vigenere Cipher")
    print("3. Choose OTP Cipher")

    choice = input("Enter the number of your choice: ")


    if choice == '1':
        option_ceasar_cipher()
    elif choice == '2':
        option_vigenere_cipher()
    elif choice == '3':
        option_otp_cipher()
    else:
        print("Not a valid option, try again")
        # recursively call main to go back to try again
        main()

if __name__ == "__main__":
    main()