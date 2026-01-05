
# List the names
names = ["Dave", "Rayan", "Zac", "mohamed", "omar", "samy", "hassin"]

# Get the name to search for 
search_name = input("Enter the name to search: ")

# Check if the name is in the list
if search_name.lower() in[name.lower()  for name in names]:
       print(search_name + "was found in the list!") # Name found
       
else:              # Name not found
    print(search_name + "was not found in the list!. ")





