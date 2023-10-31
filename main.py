#Andria Subhit (Owner), Anthony Le
#Lab 6
#10-24-23

# Andria
def encoder(password):
    encoded_str = ""    # will hold the new, updated string

    translator = {'0': '3', '1': '4', '2': '5', '3': '6', '4': '7', '5': '8', '6': '9', '7': '0', '8': '1', '9': '2'}

    for i in password:  # for every character in the string, the dictionary will give its translated equivalent
        temp = translator[i]
        encoded_str += temp

    return encoded_str

# Anthony
def decoder(encrypted_password):
    # dictionary used to subtract three (or add 7 if less than 2);
    # essentially reverts changes made from encoder() function
    translator_2 = {'0': '7', '1': '8', '2': '9', '3': '0', '4': '1', '5': '2', '6': '3', '7': '4', '8': '5', '9': '6'}
    decoded_str = ""

    # for every digit in the encrypted password,
    for i in encrypted_password:
        temp = translator_2[i]
        decoded_str += temp

    return decoded_str


def main():
    # Andria
    menu_repeats = True
    while menu_repeats:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

        choice = int(input("Please enter an option: "))

        if choice == 1:
            password = input("Please enter your password to encode: ")
            storage = encoder(password)     # stores the translated password to be called upon later

            print("Your password has been encoded and stored!\n")

        # Anthony
        elif choice == 2:
            # decrypts encrytped string, then shows both encrypted and unencrypted passwords to the user.
            decoded_str = decoder(storage)
            print(f"The encoded password is {storage}, and the original password is {decoded_str}.")

        # Andria
        elif choice == 3:
            menu_repeats = False # stops program

if __name__ == "__main__":
    main()