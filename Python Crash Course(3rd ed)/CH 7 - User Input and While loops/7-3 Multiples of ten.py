userNumber = int(input("Enter a number and I will tell you if it is a multiple of ten: "))

if userNumber % 10 == 0:
    print(f"{userNumber} is a multiple of 10")
else:
    print(f"{userNumber} is not a multiple of 10")