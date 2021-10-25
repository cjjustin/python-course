# lecture 53
name = input("enter your name please: ")
age = int(input("enter your age please: "))

if 18 <= age <= 30:
    print("Welcome to club holidays: {}".format(name))
else:
    print("Sorry we cant allow you for the holiday :)")
