age = 24
today = "on this day"
print("my age is " + str(age) + " years")

print("my age is {0} years".format(age))

print("my age is {0} years {1}".format(age, today))

print("my age is {0} years {1} {2} {3} {4}".format(24, "on this day", "and it", "is my", "birthday."))

print("jan:{0},feb:{2},mar:{1},april:{0}".format(30,31,28))
print()
print("""jan:{0}
feb:{2}
mar:{1}
april:{0}
""".format(30,31,28))