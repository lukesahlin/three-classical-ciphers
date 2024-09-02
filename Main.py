def option_ceasar_cipher():
    # running ceasar cipher
    print("Running ceasar cipher")
    message = input("Enter the message to encrypt/decrypt: ")
    action = input("Do you want to (e)ncrypt or (d)ecrypt: ").lower()
    key = input("Enter the key for encryption/decryption (a letter): ")

    if action == 'e':
        print("Encrypting message in Ceasar Cipher")
        # logic here for ceasar encryption
    if action == 'd':
        print("Decrypting message in Ceasar Cipher")
        # logic here for ceasar decryption
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
    if action == 'd':
        print("Decrypting message in Vigenere Cipher")
        # logic here for vigenere decryption
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
        print("Encrypting message in OTP Cipher")
        # logic here for otp encryption
    if action == 'd':
        print("Decrypting message in OTP Cipher")
        # logic here for otp decryption
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