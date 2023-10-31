#Andria Subhit
#Lab 6
#10-24-23

def encoder(password):
    encoded_str = ""

    translator = {'0': '3', '1': '4', '2': '5', '3': '6', '4': '7', '5': '8', '6': '9', '7': '0', '8': '1', '9': '2'}

    for i in password:
        temp = translator[i]
        encoded_str += temp

    return encoded_str

def main():
    menu_repeats = True
    while menu_repeats:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

        choice = int(input("Please enter an option: "))

        if choice == 1:
            password = input("Please enter your password to encode: ")
            storage = encoder(password)

            print("Your password has been encoded and stored!\n")
