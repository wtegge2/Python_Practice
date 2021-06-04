# This program displays a numbered list, and it also shows some useful methods to use with numbered lists. 
# Using the range() method, you can create a list of numbers starting at a specific value and ending at a specific value.
# It is important to note that the end value you enter will not be included in the list.

# min() method is used to print the minimum value of the list

# max() method is used to print the maximum value of the list

# sum() method is used to find the sum of every value of the list


# task 1 
for numbers in range(1, 21):
    print(numbers)

# task 2
numbers = list(range(1, 1000001))
for number in numbers:
    print(number)

# task 3
numbers = list(range(1, 1000001))

r1 = min(numbers)
print(r1)
r2 = max(numbers)
print(r2)
r3 = sum(numbers)
print(r3)


# task 4

