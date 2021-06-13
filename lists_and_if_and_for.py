
# This file is an excercise in which I commbine lists with if statements and for loops. 

# Initialized the list with some values
usernames = ['weeWilly123', 'Bryguy7', 'admin', 'Noobmaster69', 'SisterSky400']

if usernames:       # if statement at the beginning to test whether the list is empty or not
    for name in usernames:      # if the list is not empty, then the program runs the for loop
        if name == 'admin':         # looks for the value admin in the list and prints a special message when it finds it
            print("Hello Admin! What would you like to do today? You have many options because you are the admin.")

        else:               # prints message for every value but admin
            print(f"Hello {name}! What would you like to do?")

else:       # if the list is empty, prints message
    print("No users! We need to find some users!")

