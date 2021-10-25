parrot="norwegian blue"
letter=input("enter character")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("no such characters")