# 4.1 case sign up
username = input("Enter your username:")
email = input("Enter your email address:")
password = input("Enter your password:")
# 4.2
passwordCheck = input("Retype your password:")
if ("@" in email) and (len(email) > 8):
    if (passwordCheck == password):
        print("sign up success")
else:
    print("Email inappropriate")

isDone = True

while isDone:
    email = input("Enter your email: ")
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    repassword = input("Reenter password: ")

    if ("@" in email) and (len(password) >= 8):
        if (repassword == password):
            print("Sign up success")
            isDone = False
        else:
            print("Wrong password")
    else:
        print("Password need to have atleast 8 Character"
