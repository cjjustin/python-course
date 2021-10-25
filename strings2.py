#                 1
#       0123456789012
parrot="norwiean blue"
print(parrot)
print(parrot[3])

print(parrot[-1])
print(parrot[-13])
print()


# minichallenge negative index
print(parrot[-10])
print(parrot[-8])
print()
print(parrot[-10])
print(parrot[-9])
print(parrot[-13])

print()

# slicing
print(parrot[0:6]) #last index is not included
print(parrot[:6])
print(parrot[9:13])
print(parrot[9:])

print(parrot[:]) #print whole string

print(parrot[0:6:2]) #step slice
print(parrot[0:6:3])


number="2,354:128,124;121 243.123"
seperators=number[1::4]
print(seperators)

values="".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])


#lecture 56
number="2,354:128,124;121 243.123"
seperators=""
for i in number:
    if not i.isnumeric():
        seperators+=i
print(seperators)

#lecture 57
values="".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])