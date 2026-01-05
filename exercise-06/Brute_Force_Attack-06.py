# Define the correct password
correct_password = 12345

# Maximim number of allowed attempts
max_attempts = 5

# Counter for attempts
attempts = 0

# Loop until attempts reach the limit
while attempts < max_attempts:

    # Ask the user to enter the password
    password = int(input("enter the password: "))

    # Check if the entered password is correct
    if password == correct_password:
        # if the password is correct, access is granted
        print("access granted. Correct password!")
        break # Stop the loop

    else:
        # Increase attempts
        attempts += 1

        # Calculate remaining attempts
        remaining = max_attempts - attempts
        # Show remaining attempts or final warning
        if remaining > 0:
            print("wrong password. remaining attempts:", remaining)
        else:
            print("Maximum attempts reachad. Authorities have been alerted!")
