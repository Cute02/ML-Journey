# Check if a number is unique
org = []
num=int(input("Enter the number u want to check: "))
digits=str(num)
for i in digits:
    if i in org:
        break
    else:
        org+=i

    

