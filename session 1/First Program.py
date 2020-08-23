# how to draw with a turtle

import turtle
turtle.shape("turtle")
# this is to summon the turtle
# 
for i in range(5):
    turtle.forward(100) 
    turtle.right(144)
# this is the loop

turtle.mainloop()
# you need this at the end when drawing or doing some other shits

# valuable name = "blah blah" (note valuable name cannot contain space or any special symbols)
# name = "hiep" (correct)
# City name = Hanoi (wrong because there is a space between "city" and "name").

age = "16.2"
name = "vapour"
print("hello " + name,age)

# special stuff lmao

name = input("Enter your name:")
print('hello' + name)

#let n = a value then do the math lmao.

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = (a + b)/2

# + addition, - subtraction, * multiplication, / division.
print(c)

# range(n)
# start = 0, stop = n, step = 1


print(*range(11))
print(*range(0, 102, 2))

