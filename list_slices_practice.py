
star_wars_characters = ['luke skywalker', 'darth vader', 'han solo', 'chewbacca', 'jabba', 'boba fett']

print("The first three items in the list are: ")
print(star_wars_characters[:3])

print("The middle items in the list are: ")
print(star_wars_characters[1:5])

print("The last three items of the list are: ")
print(star_wars_characters[3:])


my_food = ['Pizza', 'Taco', 'Apple', 'Cheeseburger']
friends_food = my_food[:]

my_food.append('Chips')

friends_food.append('Carrot')

print("My favorite foods are: ")
for food in my_food:
    print(food)

print("My friend's favorite foods are: ")
for friend_food in friends_food:
    print(friend_food)

