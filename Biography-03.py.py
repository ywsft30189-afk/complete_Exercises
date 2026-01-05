
# Ask user for full name
name = input("enter your full name: ")
# Ask user for hometown
town = input("enter your hometown: ")

# Ask user for age and check it's a number
while True:
    age_text = input("enter your age (must be a number): ")
    try:
        age = int(age_text)  # Convert to integer
        break   # Exit loop if successful
    except ValueError:
        print("Invalid input! please enter a number for age.")


# Store data in a dictionary
bio = {
        "Name" : name,
        "Hometown": town, 
        "Age": age

    }

 # Print all information on separate lines
print(bio["Name"], "\n" + bio["Hometown"], 
          "\n" + str(bio["Age"]))
    
     