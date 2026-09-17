class MyError(Exception):
    pass


def check_age(age):
    if age <= 0:
        raise MyError("Number can't be less than zero")
    return age


repeat = 1

while repeat == 1:

    try:
        user_age = int(input("Enter your age : "))
        valid_age = check_age(user_age)
        print("valid age : ", valid_age)
        repeat = 0
    except ValueError:
        print("The value not number, Enter a valid number")
    except MyError as e:
        print(e)
    finally:
        if repeat:
            print("countinue . . .")
            print()
        else:
            print("Ending . . .")
print("Ended")
