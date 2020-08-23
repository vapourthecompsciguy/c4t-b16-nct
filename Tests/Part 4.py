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

