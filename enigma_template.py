from random import randint

running = True


while running == True:
    print("Welcome to Enigma Machine \n Please select an option")
    print("[1]: Ecode a custom message \n [2]: Encode file. \n [3]: Decode file. \n [4]: Exit.")

    try:
        choice = int(input("choose and option"))

        if 0 > choice or choice > 4:
            print("that isn't an option")
            continue

        if choice == 1:
            message = input("Please enter the message you'd like to encode: ")
            rotate = int(input("Enter the rotational cipher key. (press enter for a random value")) or randint(1, 26)

        elif choice == 2:

        elif choice == 3:

        elif choice == 4:
            exit()




    except ValueError:
        print("you got a value error")
