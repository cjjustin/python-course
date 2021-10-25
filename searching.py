shopping = ["milk", "eggs", "bread", "butter"]

for item in shopping:
    if item == "eggs":
        print("found " + item)
        break

find = "eggs"
foundat = None

for index in range(len(shopping)):
    if shopping[index] == find:
        foundat = index
        break
print("eggs found at:{}".format(foundat))

find="cow"
foundat = None
for index in range(len(shopping)):
    if shopping[index] == find:
        foundat = index
        break
print("{} found at:{}".format(find,foundat))


find = "eggs"
if find in shopping:
    foundat=shopping.index(find)
    print("item found at :{}".format(foundat))
else:
    print("{} not found".format(find))
