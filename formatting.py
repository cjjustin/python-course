for i in range(1, 11):
    print("{0:<2}'s square is {1:<3} ,cube is {2:<2}".format(i, i ** 2, i ** 3))

for i in range(1, 11):
    print("{0:2}'s square is {1:3} ,cube is {2:2}".format(i, i ** 2, i ** 3))

print()
print("pi approx {0:12}".format(22/7)) #general
print("pi approx {0:12f}".format(22/7))
print("pi approx {0:12.50f}".format(22/7))
print("pi approx {0:52.50f}".format(22/7))
print("pi approx {0:62.50f}".format(22/7))
print("pi approx {0:<72.50f}".format(22/7))
print("pi approx {0:<72.56f}".format(22/7))

for i in range(1, 11):
    print("{}'s square is {} ,cube is {:4}".format(i, i ** 2, i ** 3))
