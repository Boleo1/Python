prompt = "\nTell me something and I will repeat it back to you"
prompt += "\nEnter 'quit' to exit the program: "

active = True                       # This is a flag to signify if our while loop should execute or not.
message = ""
while message != 'quit':            # While loop to keep taking user input and returning the input.
    message = input(prompt)
    if message != 'quit':           # else we do not print quit to the console like we did in prior versions.
        print(message)