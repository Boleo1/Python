guestList = ['mr h', 'aaron', 'steve jobs', 'elon musk']
message = "I am having dinner and I would like you to attend."

print(f"{guestList[0].title()} {message}")
print(f"{guestList[1].title()} {message}")
print(f"{guestList[2].title()} {message}")
print(f"{guestList[3].title()} {message}")
cantAttend = []
cantAttend = guestList.pop(0)
print(f"It seems that {cantAttend[0]} cannot make it.")

guestList.insert(0, 'jeff bezos')
print(f"In place of {cantAttend[0].title()} I have invited {guestList[0].title()}")