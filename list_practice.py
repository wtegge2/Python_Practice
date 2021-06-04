# This program is all about lists! It shows how to initialize a list, and how to use individual items of the list. 
# It also shows how to manipulate items in the list such as adding and removing an item. 



# LIST
friends = ['Antonio', 'Jada', 'Bob', 'Vicky']

#ORIGINAL INVITATIONS

message1 = f"Dear {friends[0].title()}, you are invited!"
print(message1)
message2 = f"Dear {friends[1].title()}, you are invited!"
print(message2)
message3 = f"Dear {friends[2].title()}, you are invited!"
print(message3)
message4 = f"Dear {friends[3].title()}, you are invited!"
print(message4)

absent_message = f"Oh no! {friends[2]} cannot make it anymore!"
print(absent_message)

del friends[2]

friends.insert(2, 'Adrian')

new_invitation = f"{friends[2].title()} is coming now!"
print(new_invitation)


# NEW INVITATIONS
message1 = f"Dear {friends[0].title()}, you are invited!"
print(message1)
message2 = f"Dear {friends[1].title()}, you are invited!"
print(message2)
message3 = f"Dear {friends[2].title()}, you are invited!"
print(message3)
message4 = f"Dear {friends[3].title()}, you are invited!"
print(message4)
