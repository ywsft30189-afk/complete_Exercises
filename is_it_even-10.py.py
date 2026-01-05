# function to check if the number is even or odd
def is_even_or_odd(number):
    # Check remainder when dividing by 2
    if number % 2 == 0:
        return "the number is even"
    else:
        return "the number is odd"
    
# Main function
def main():
    # Ask user to enter a number
    user_number = int(input("Enter a number: "))

    # Call the function and store the result
    result = is_even_or_odd(user_number)

    # Print the result
    print(result)

# Run the main function
main()
