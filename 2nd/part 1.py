# # 1
# x = int(input("Enter first number:"))
# y = int(input("Enter second number:"))

# def checkNumber():
#     if x < y:
#         return(y, "is larger than", x)
#     if y < x: 
#         return(x, "is larger than", y)
#     else:
#         return("Two numbers are equal")

# print(checkNumber())

# # 2

# def check_odd_even(numbers):
#     if numbers % 2 == 0:
#         return("This is an even number")
#     else:
#         return("this is an odd number")
# number = int(input("Enter a number:"))
# result = check_odd_even(number)
# print(result)

# # 3
# def check_year(year):
#     if year % 4 == 0:
#         return("This is a leap year")
#     else:
#         return("Thí is a normal year")
# year = int(input("Enter a year:"))
# result = check_year(year)
# print(result)

# 4
user_list = [12, 'hiep', 56, 'student', False, 2019]
listNumber = []

def check_type_of_function(input):
    if type(input) is list:
        return True
    else:
        return False

def totalFunc(allNumb):
   

    for i in allNumb:
        if type(i) is int:
            listNumber.append(i)

    return sum(listNumber)

while True:
    if check_type_of_function(user_list):
        print(totalFunc(user_list))
        break
    else:
        print("This is not a list.")





