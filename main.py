def encoder(password):
    global new_password
    new_password = ''
    for i in password:
        if i == '7':
            new_password += '0'
        elif i == '8':
            new_password += '1'
        elif i == '9':
            new_password += '2'
        else:
            new_password += str(int(i) + 3)
    return new_password


def main():

    while 0 == 0:
        print("Menu\n"
              "-----------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        user_choice = input("Please enter an option: ")

        if user_choice == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!\n")

        elif user_choice == '2':
            print(f"The encoded password is {new_password}, and the original password is {password}\n")

        elif user_choice == '3':
            break

main()




