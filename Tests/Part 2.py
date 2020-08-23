# 2.1
print(*range(3, 13, 1))

# 2.2
n = int(input("Enter Final Number:"))
if n > 0:
    print(*range(0, n + 1, 1))
else:
    print("n must be > 0")

# 2.3a

a = int(input("Enter Final Number:"))
for num in range(a + 1, 0 , -1):
    if num % 2 != 0: 
        print(num, end = " ")

# 2.4
import turtle
turtle.shape("turtle")
t = turtle.Turtle()
z = int(input("Enter the no of the sides of the polygon : ")) 
for _ in range(z): 
    turtle.forward(100) 
    turtle.right(360 / z) 
turtle.mainloop()
