
from caesar import caesar_decryption, caesar_encryption
from one_time_pad import decrypt_one_time_pad, encrypt_one_time_pad
from vigenere import decrypt_vigenere, encrypt_vigenere


def option_caesar_cipher():
    """
    Prompts the user to encrypt or decrypt a message using the Caesar cipher.
    
    The user is asked to provide a message and a key (a letter) for encryption or decryption.
    If the user selects encryption, the function calls `caesar_encryption`, 
    otherwise it calls `caesar_decryption`. The result is saved to a file.

    Recursively handles invalid inputs or key lengths, and allows the user to quit 
    by entering '4' at any prompt.
    """
    
    # running caesar cipher
    print("Running caesar cipher")
    print("To quit, please enter '4' during any prompt")
    message = input("Enter the message to encrypt/decrypt: ")
    if message == '4':
        exit()
    if not contains_only_letters(message):
        print("The message can only contain letters and spaces. Try again.")
        option_caesar_cipher()
        return
    action = input("Do you want to (e)ncrypt or (d)ecrypt: ").lower()
    if action == '4':
        exit()
    key = input("Enter the key for encryption/decryption (a letter): ")
    if key == '4':
        exit()
    if not contains_only_letters(key):
        print("The message can only contain letters and spaces. Try again.")
        option_caesar_cipher()
        return

    if action == 'e':
        print("Encrypting message in Caesar Cipher")
        cipher_text = caesar_encryption(message.upper(), key.upper())
        export_cipher_to_file(cipher_text, "Ceasar Encryption")
        return
    if action == 'd':
        print("Decrypting message in Caesar Cipher")
        cipher_text = caesar_decryption(message.upper(), key.upper())
        export_cipher_to_file(cipher_text, "Ceasar Decryption")
        return
    else:
        print("Not a valid selection, please choose 'e' for encrypt and 'd' for decrypt.")
        option_caesar_cipher() # recursively call function to go back again


def option_vigenere_cipher():
    """
    Prompts the user to encrypt or decrypt a message using the Vigenere cipher.

    The user is asked to provide a message and a key (a word) for encryption or decryption.
    If the user selects encryption, the function calls `encrypt_vigenere`, 
    otherwise it calls `decrypt_vigenere`. The result is displayed and saved to a file.

    Recursively handles invalid inputs or key lengths, and allows the user to quit 
    by entering '4' at any prompt.
    """

    # running the vigenere cipher
    print("Running vigenere cipher")
    print("To quit, please enter '4' during any prompt")
    message = input("Enter the message to encrypt/decrypt: ").upper()
    if message == '4':
        exit()
    if not contains_only_letters(message):
        print("The message can only contain letters and spaces. Try again.")
        option_vigenere_cipher()
        return
    action = input("Do you want to (e)ncrypt or (d)ecrypt: ").lower()
    if action == '4':
        exit()
    key = input("Enter the key for encryption/decryption (a word): ").upper()
    if key == '4':
        exit()
    if not contains_only_letters(key):
        print("The message can only contain letters and spaces. Try again.")
        option_vigenere_cipher()
        return

    if action == 'e':
        cipher_text = encrypt_vigenere(message, key)
        print("Encrypting message in Vigenere Cipher")
        print("your secret message is " + cipher_text)
        export_cipher_to_file(cipher_text, "Vigenere Encryption")
        
        return
    if action == 'd':
        secret = decrypt_vigenere(message, key)
        print("Decrypting message in Vigenere Cipher")
        print("your secret is " + secret)
        export_cipher_to_file(secret, "Vigenere Decryption")
        return
    else:
        print("Not a valid selection, please choose 'e' for encrypt and 'd' for decrypt")
        option_vigenere_cipher() # recursively call function to go back again

def option_otp_cipher():
    """
    Prompts the user to encrypt or decrypt a message using the One-Time Pad (OTP) cipher.

    The user is asked to provide a message and a key of the same length for encryption or 
    decryption. If the user selects encryption, the function calls `encrypt_one_time_pad`,
    otherwise it calls `decrypt_one_time_pad`. The result is displayed and saved to a file.

    Recursively handles invalid inputs, checks for matching key length, and allows 
    the user to quit by entering '4' at any prompt.
    """
    
    # run the otp cipher
    print("Running otp cipher")
    print("To quit, please enter '4' during any prompt")
    message = input("Enter the message to encrypt/decrypt: ")
    if message == '4':
        exit()
    if not contains_only_letters(message):
        print("The message can only contain letters and spaces. Try again.")
        option_otp_cipher()
        return
    action = input("Do you want to (e)ncrypt or (d)ecrypt: ").lower()
    if action == '4':
        exit()
    key = input("Enter the key for encryption/decryption (must be as long as the message): ")
    if key == '4':
        exit()
    if not contains_only_letters(key):
        print("The message can only contain letters and spaces. Try again.")
        option_otp_cipher()
        return

    # check if the key is equally as long as the message
    if len(key) != len(message):
        print("Key must be the same length as the message")
        option_otp_cipher()
        return

    if action == 'e':
        hiddenMessage = encrypt_one_time_pad(message, key)
        print("Encrypting message in OTP Cipher")
        print("your secret message is " + hiddenMessage)
        export_cipher_to_file(hiddenMessage, "OTP Encryption")
        return
    if action == 'd':
        secret = decrypt_one_time_pad(message, key)
        print("Decrypting message in OTP Cipher")
        print("your secret is " + secret)
        export_cipher_to_file(secret, "OTP Decryption")
        return
    else:
        print("Not a valid selection, please choose 'e' for encrypt and 'd' for decrypt")
        option_otp_cipher() # recursively call function to go back again

def contains_only_letters(input_string):
    """
    Checks if a given string contains only alphabetic characters and spaces.

    Args:
        input_string (str): The string to be checked.

    Returns:
        bool: True if the string contains only letters and spaces, False otherwise.
    """
    
    return all(char.isalpha() or char.isspace() for char in input_string)


def export_cipher_to_file(cipher_text, cipher_type):
    """
    Saves the cipher text and its type to a file.
    
    Args:
        cipher_text (str): The encrypted or decrypted message.
        cipher_type (str): The type of cipher used (e.g., 'Caesar', 'Vigenere', 'OTP').

    Creates a file with the format "{cipher_type}_cipher.txt" and appends the
    cipher text and type to the file.
    """
    
    filename = f"{cipher_type}_cipher.txt"
    with open(filename, "a") as file:
        file.write(f"Cipher type: {cipher_type}:\n")
        file.write(f"Cipher text: {cipher_text}\n")
        file.write("\n")
        file.close()
    print(f"Cipher text and type have been exported to {filename}")

def main():
    """
    Main function to run the cipher selection interface.

    Prompts the user to choose between Caesar, Vigenere, and OTP ciphers, or to quit.
    Based on the selection, the corresponding function (`option_caesar_cipher`, 
    `option_vigenere_cipher`, or `option_otp_cipher`) is called.

    Invalid selections are handled recursively.
    """
    
    # test
    print("Choose an option of what cipher to use:")
    print("1. Choose Caesar Cipher")
    print("2. Choose Vigenere Cipher")
    print("3. Choose OTP Cipher")
    print("4. Quit")

    choice = input("Enter the number of your choice: ")


    if choice == '1':
        option_caesar_cipher()
    elif choice == '2':
        option_vigenere_cipher()
    elif choice == '3':
        option_otp_cipher()
    elif choice == '4':
        exit()
    else:
        print("Not a valid option, try again")
        # recursively call main to go back to try again
        main()

if __name__ == "__main__":
    main()