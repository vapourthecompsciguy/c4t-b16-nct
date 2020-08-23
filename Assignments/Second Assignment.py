
# a = int(input("Input length:"))
# b = int(input("Input length:"))
# c = int(input("Input length:"))

# s = (a + b + c)/2
# A = (s * (s - a) * (s - b) * (s - c))**0.5
# print(A)

# if (a == c):
#     print("Isosceles Triangle")
# elif (b**2 == a**2 + c**2):
#     print("Right-angle Triangle")
# else:
#     print("Normal Triangle")

# .................................................................................................................................................................

# books = [
#     "Books 1", "Harry Potter", "Romeo Juliet", "Su tich cay khe", "Thach Sanh"
# ]

# while True:
#     userInput = input("enter here:")
#     if userInput in books:
#         index = books.index(userInput)
#         print(books[index])
#         break
#     else:
#         print("Not found")

# .............................................................................................................................................................

from random import *
a = randrange(10)
b = randrange(10)
correct = a + b
n = randint(-1, 1)
incorrect = correct + n

print(a, "+", b, "=", incorrect)
userInput = input("True or False (T/F):")

if correct != incorrect:
    if userInput.lower() == "t":
        print("You lose")
    elif userInput.lower() == "f":
        print("You Win")
else:
    if userInput.lower() == "t":
        print("You win")
    elif userInput.lower() == "f":
        print("You lose")


    
