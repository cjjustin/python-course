for i in range(1, 13):
    print("No. {} squared as {} and cubes as {:4}".format(i, i ** 2, i ** 3))
print("*" * 80)
for i in range(1, 13):
    print("No. {} squared as {} and cubes as {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80)

name = input("enter your name")
age = int(input("how old are you,{}?".format(name)))
print(age)
# if age > 18:
#     print("can vote")
#     print("drop your vote in the respected box")
# else:
#     print("come back in {} years".format(18-age))

if age > 18:
    print("can vote")
    print("drop your vote in the respected box")
elif age == 18:
    print(name+" register yourself with voting authorities ")
    print("Then drop your vote in the respected box")
else:
    print("come back in {} years".format(18-age))

