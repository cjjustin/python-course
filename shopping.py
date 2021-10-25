shopping = ["milk", "eggs", "bread", "butter"]

for item in shopping:
    if item != "butter":
        print("buy:" + item)

for item in shopping:
    if item == "butter":
        continue
    print("buy:" + item)


