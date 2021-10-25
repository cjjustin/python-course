ans = 5

print("please guess a number between 1 and 10:")
guess = int(input())
# if guess<ans:
#     print("please guess higher")
# elif guess > ans:
#     print("please guess lower")
# else:
#     print("you got it first time")

# conditional
if guess != ans:
    if guess < ans:
        print("please guess higher")
    else:
        print("please guess lower")
        print("guess once more")
    guess = int(input())
    if guess == ans:
        print("You guessed it right")
    else:
        print("sorry you guessed it wrong")
else:
    print("you got it first time")



# if elif conditional challenge lecture 46
if guess == ans:
    print("you got it first time")

else:
    if guess < ans:
        print("please guess higher")
    else:
        print("please guess lower")
    print("guess once more")
    guess = int(input())
    if guess == ans:
        print("You guessed it right")
    else:
        print("sorry you guessed it wrong")
