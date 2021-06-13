# This file demonstrates the use of if-elif-else statements 

rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']


if 'pink' in rainbow_colors:            # This first test tests a value not in the list, so the test fails and it moves on to the next test
    print("Pink is a color of the rainbow!")

elif 'red' in rainbow_colors:           # This test passes, so the block of code that is after it will be executed
    print("Red is a color of the rainbow!")

elif 'orange' in rainbow_colors:        # This test does not run because an if-elif-else statement only allows one test to pass and does not run the other tests
    print("Orange is a color of the rainbow!")

