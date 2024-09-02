def option_ceasar_cipher():
    # running ceasar cipher
    print("Running ceasar cipher")


def option_vignere_cipher():
    # running the vignere cipher
    print("Running vignere cipher")

def option_otp_cipher():
    # run the otp cipher
    print("Running otp cipher")


def main():
    print("Choose an option of what cipher to use:")
    print("1. Choose Ceaser Cipher")
    print("2. Choose Vignere Cipher")
    print("3. Choose OTP Cipher")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        option_ceasar_cipher()
    elif choice == '2':
        option_vignere_cipher()
    elif choice == '3':
        option_otp_cipher()
    else:
        print("Not a valid option, try again")
        # recursively call main to go back to try again
        main()

if __name__ == "__main__":
    main()