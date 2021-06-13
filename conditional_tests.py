game_of_thrones_characters = ['jon snow', 'arya stark', 'sansa stark', 'tyrion lannister', 'the hound']

new_character = 'khaleesi'

if new_character not in game_of_thrones_characters:
    game_of_thrones_characters.append(new_character)

if new_character in game_of_thrones_characters:
    print(f"{new_character.title()} is already in the list!" )


