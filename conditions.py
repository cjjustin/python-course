age = int(input("how old are you?"))
# if age >= 16 and age <= 65:
if 16<=age<=65:
    print("you can apply for the role")
else:
    print("You cannot apply for the role")
print("-"*40)


#lecture 59
if age in range(16,66):
    print("you can apply for the role")
else:
    print("You cannot apply for the role")
print("-"*40)