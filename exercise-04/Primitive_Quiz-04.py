# List of countries (in lowercase to match user input easily)
countries = ["france", "germany", "italy", "spain", "united kingdom", "netherlands", "sweden", 
             "poland", "greece", "portugal"]

# List of capitals in the same order as the countries List
capitals = ["paris", "berlin", "rome", "madrid", "london", "amsterdam",
            "stockholm", "warsaw", "athens", "lisbon"]

# Display the quiz title so the user knows what the program is about
print("== capitals cities quiz == ")
print("---------------------------")
# display the list of countries
print("\nCountries:")
print("-------------")
for country in countries:
   print(country.title())

# print a separator line for better readability
print("\n-------------------------\n")


# Variable to  store the user's score
score = 0

# Loop through each country using its index
for i in range(10):
         
    # Ask the user to enter the capital of the current country
    city = input(f"what is the capital of {countries[i].title()}?").strip().lower()

    # Store the correct capital for comparison
    correct = capitals[i]

    # Check if the user's answer matches the correct capital
    if city == correct:
        print("correct answer!")
        print("your answer is correct ")

        # Increase score for a correct answer
        score += 1
    else:
        print("wrong answer!")

        # Show the correct answer if the user is wrong
        print(f"the correct answer is: {correct.title()}")

    # Print an empty line between questions
    print()

# Display the final score after all questions are answered
print(f"your final score: {score}/10")
