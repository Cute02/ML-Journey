a = int(input("Enter 2 numbers"))  # 4
b = int(input())  # 3


def method1(a, b):
    a = a+b  # a=7
    b = a-b  # b=4
    a = a-b  # a=3
    print("a", a, "b", b)


def method2(a, b):
    temp = a
    a = b
    b = temp
    print("a= ", a, "b= ", b)


print("Menu\n1.temp method\n2.Arithmetic method\n3.Exit")

choice = int(input("Enter your choice: "))
if choice == 1:
    method1(a, b)
elif choice == 2:
    method2(a, b)
elif choice == 3:
    print("Exiting....Thank You")
