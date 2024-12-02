from random import randint  # Import randint to generate random rotational keys

# Function to encode or decode a message using a rotational cipher
def cypher(message, rotate, type):
    """Apply a rotational cipher to the given message."""
    for x in message:
        if x in let:  # Check if the character is lowercase
            val = (let.index(x) + int(rotate)) % 26  # Calculate the new index after rotation
            message = message.replace(x, let[val])  # Replace character with the rotated character
        elif x in Clet:  # Check if the character is uppercase
            val = (Clet.index(x) + int(rotate)) % 26  # Calculate the new index for uppercase letters
            message = message.replace(x, Clet[val])  # Replace character with the rotated character
        else:
            continue  # Skip non-alphabet characters

    print(f"Used key of {rotate}, {type}d message is: {message}")  # Print the result

# Initialize variables
running = True  # Control the main loop

let = 'abcdefghijklmnopqrstuvwxyz'  # Define lowercase alphabet
Clet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Define uppercase alphabet

# Main loop for user interaction
while running == True:
    print("Welcome to Enigma Machine \n Please select an option")
    print("[1]: Encode a custom message \n [2]: Encode file. \n [3]: Decode file. \n [4]: Exit.")

    try:
        # Get the user's choice and validate input
        choice = int(input("choose an option: "))

        if 0 > choice or choice > 4:  # Validate that the choice is within the valid range
            print("That isn't an option")
            continue  # Restart the loop if invalid

        if choice == 1:
            # Option 1: Encode a custom message
            fmessage = input("Please enter the message you'd like to encode: ")
            # Get the rotation key or generate a random one if the user presses Enter
            turn = input("Enter the rotational cipher key. (press enter for a random value)") or randint(1, 26)
            cypher(fmessage, turn, "encode")  # Call the cypher function to encode the message

        elif choice == 2:
            # Option 2: Encode a message from a file
            file = open(input("Please enter the filename of the message you'd like to encode: "), "r")
            fmessage = file.read()  # Read the content of the file
            turn = input("Enter the rotational cipher key. (press enter for a random value)") or randint(1, 26)
            cypher(fmessage, turn, "encode")  # Call the cypher function to encode the file content

        elif choice == 3:
            # Option 3: Decode a message from a file
            file = open(input("Please enter the filename of the message you'd like to decode: "), "r")
            fmessage = file.read()  # Read the content of the file
            turn = input("Enter the rotational cipher key. (press enter if unknown)") or None

            if turn == None:
                # If the key is unknown, try all possible rotations
                print("Unknown key detected. Printing all possible rotations:")
                for turn in range(26):  # Iterate through all possible shifts
                    cypher(fmessage, int(turn) * -1, "decode")  # Decode using each rotation
            else:
                cypher(fmessage, int(turn) * -1, "decode")  # Decode using the provided key

        elif choice == 4:
            # Option 4: Exit the program
            exit()  # Terminate the program

    except ValueError:
        print("You got a value error")
