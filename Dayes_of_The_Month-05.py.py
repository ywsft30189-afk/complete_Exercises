# Stores days in each month
days_in_month = {
    1: 31,    # January
    2: 28,    # February (non-leap year)
    3: 31,    # March
    4: 30,    # April
    5:  31,   # May
    6:  30,   # June
    7:  31,   # July
    8:  31,   # August
    9:  30,   # September
    10: 31 ,  # October
    11: 30,   # November
    12: 31    # December
}

# welcome message
print("=" *40)
print("Days of the month calculator")
print("=" * 40)
# Ask the user to input the month number
month_num = int(input("Enter the month number (1-12): "))

# Check if the entered month number is valid
if month_num < 1 or month_num > 12:
    print("invalid month number!\n please enter a numbr from 1 to 12.")
else:
    # if the month is February, ask if it is a leap year
    if month_num == 2:
        leap = input("is it a leap year? (yes/no): ").strip().lower()
        if leap == "yes":
            print("February has 29 days.")
        else:
            print("February has 29 days.")
    else:
        # For all other months, print the number of days from the dictionary
        print(f"this month has {days_in_month[month_num]} days.")