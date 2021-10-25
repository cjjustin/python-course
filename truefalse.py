day = "Monday"
temp = 30
raining = False

if day == "Saturday" and temp > 27 and not raining:
    print("go swimming")
else:
    print("learn python")

day = "Monday"
temp = 30
raining = False

if (day == "Monday" and temp > 27) or not raining:
    print("go swimming")
else:
    print("learn python")

if 0:
    print("true")
else:
    print("false")

name = input("enter name:")
if name:
#if name !="":
    print("hello {}".format(name))
else:
    print("man with no name")
