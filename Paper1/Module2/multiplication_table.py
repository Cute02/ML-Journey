multiplier = int(input("which number's multiplction table u need? "))
num = int(input("Enter the limit: "))
for i in range(1, num+1):
    print(f"{multiplier} * {i} = {multiplier*i}")
