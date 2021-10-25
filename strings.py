print('today is a good day')
print('python is fun')
print("we can include 'quotes' in python")
print("we can include 'quotes' in python" + '3')
greet = "hello"
name = input("enter your name")
print(greet + " " + name)

age = 24
print(age)

print(type(greet))
print(type(age))

ageiny= "2 years"
print(type(ageiny))

#print("name is "+name+ " age is"+ age) shows error

print("name is "+name+ f" age is {age}") # added f to take value inside quotes

print(f"pi approx is {22/7:12.50f}") #f-string formatting
pi=22/7
print(f"pi approx is {pi:12.50f}") #same as above