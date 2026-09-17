class AgeError(Exception):
    "Raised when person error is less than 18..."


try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeError
except AgeError:
    print("Person not eligible for voting..")
else:
    print("Person is eligible for voting..")
