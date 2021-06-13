
# This file is my first practice with using conditional statements with lists. 
# I started out with a list of characters from one of my favorite shows, and then I 
# use conditional statements to determine if a character is in the list or not. 
# If the character is not in the list, then it is added to the end of the list.
# If the character is in the list, then it prints a message saying that is is already in the list.


game_of_thrones_characters = ['jon snow', 'arya stark', 'sansa stark', 'tyrion lannister', 'the hound']

new_character = 'khaleesi'

if new_character not in game_of_thrones_characters:
    game_of_thrones_characters.append(new_character)

if new_character in game_of_thrones_characters:
    print(f"{new_character.title()} is already in the list!" )


