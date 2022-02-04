from getpass import getpass
import os


def hem(ans):
    print(eval(ans))


UserName = input("ENTER YOUR USERNAME:")
print("Your username is your password")
Password = getpass("Enter PASSWORD: ")


def user():
    print(UserName)


if UserName == Password:
    print("Your Login is Successful..!!")
    menu = input("to continue press 1:")
    if menu == "1":
        NewMenu = input("""1.TO RUN CALCULATOR
2.TO OPEN INSTALLED APPS
3.TO PRINT YOUR USERNAME  :: """)
        if NewMenu == "1":
            cal = input("Enter Expression:")
            hem(cal)

        elif NewMenu == "2":
            app = input("ENTER THE APP NAME")
            run = os.system(app)
            print(run)
        elif NewMenu == "3":
            user()
    else:
        exit()
else:
    print("AUTHENTICATION ERROR")
