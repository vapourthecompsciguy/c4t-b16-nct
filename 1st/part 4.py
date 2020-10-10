# 1
numberList = [5, 1, 8, 92, 7, 30]
even_number = [num for num in numberList if num % 2 == 0] 
print("Even numbers in the list: ", even_number) 

# 2
userList = input("Enter a list of numbers, serperated by ',':")
userList = userList.split(',')
total = 0
for i in userList:
    total += int(i)

print("Sum of all entered numbers:", total)