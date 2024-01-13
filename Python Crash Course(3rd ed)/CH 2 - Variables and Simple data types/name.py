# Showcasing the string operators and how they can be used, also using f string formatting.

name = "anthony beaulieu"
print(name.title())

first = "anthony"
last = "beaulieu"

print(first.upper())
print(first.lower())  # .lower() is good for storing user inputted data to a file or database without the need for user manipulation and breaking the data table.

print(f"{first.capitalize()} {last.capitalize()}")  # f string usage, allows for variables to be called mid string with curly braces.

message = f"Hello, {name.title()}"  # f strings can also be stored in variables.
print(message)

whitespace = "   Hello "
print(whitespace)

print(whitespace.lstrip())
print(whitespace.strip())

url = "https://www.github.com/boleo1"
url = url.removeprefix("https://www.")
print(url)