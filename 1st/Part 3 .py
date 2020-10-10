

# 1
numberList = [5 , 1, 8, 92, -1, 30]
userInput = int(input("enter a number:"))
if userInput in numberList:
    print("Found, position:", numberList.index(userInput))
else:
    print("Not Found in our list:")

# 2
print(sum(numberList))

# 3
userList = input("Enter a list of numbers, serperated by ' ':")
userList = userList.split(' ')
total = 0
for i in userList:
    total += int(i)

print("Sum of all entered numbers:", total)