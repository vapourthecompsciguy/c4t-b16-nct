# 3.1
n = int(input("Enter number:"))
if n > 13:
    print("this number is greater than 13")
elif n == 13:
    print("This number is equal to 13")
else:
    print("this number is smaller than 13")

# 3.2
a = int(input("Enter number:"))
if a % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

# 3.3
m = input("Enter month:")
if m == 'January' or m == 'March' or m == 'May' or m == 'July' or m == 'April' or m == 'October' or m == 'December':
    print("31 days")
elif m == 'February':
    print("28 days or 29 days if its a leap year")
elif m == 'April' or m == 'June' or m == 'September' or m == 'November':
    print("30 days")
else:
    print("Insert a month please")