current_users = ['username45', 'Flash22', 'I_AM_BATMAN', 'Sir_Booty21', 'LadyNobodyhhh']

new_users = ['Flash22', 'WhoCaresAboutAnyone', 'PrtyLyfe420', 'COOLBEATZ', 'I_AM_BATMAN']

for name in new_users:
    if name in current_users:
        print("That username is taken. Please pick a different username.")

    else:
        print("That username is available!")


# /////////////////////////////////////////////////
# Seperate excercise

numbers = list(range(1,10))
print(numbers)

for number in numbers:
    if number == 1:
        print(f"{number}st ")
    elif number == 2:
        print(f"{number}nd ")
    elif number == 3:
        print(f"{number}rd ")
    elif number > 3:
        print(f"{number}th ")

        


    


