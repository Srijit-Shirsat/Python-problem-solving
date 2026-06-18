# Assignment 4

username=input("Enter your username: ")
password=input("Enter your password: ")
account_status=input("Enter account status: ")

if username!="admin":
    print("LOGIN FAILED: INVALID USERNAME")
else:
    if password!="python123":
        print("LOGIN FAILED: INVALID PASSWORD")
    else:
        if account_status!="active":
            print("LOGIN FAILED: ACCOUNT INACTIVE")
        else:
            print("LOGIN SUCCESS")

        