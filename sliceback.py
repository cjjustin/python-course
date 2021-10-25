letters="abcdefghijklmnopqrstuvwxyz"

backwards= letters[25::-1]
print(backwards)
print()
backwards= letters[::-1]#backward idiom
print(backwards)

#challenge
backwards= letters[16:13:-1]#qpo
print(backwards)
print()
backwards= letters[4::-1]#edcba
print(backwards)
print()
backwards= letters[:17:-1]#last 8 = zyxwvuts
print(backwards)
print()
print(letters[-4:])#last4
print(letters[-1:])#last1