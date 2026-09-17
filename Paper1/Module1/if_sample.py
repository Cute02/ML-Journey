print("Menu\n1.Mandhi\n2.KFC\n3.Biriyani\n4.Meals\n5.Ice cream")
item_no = int(input("Enter the item no. you want....."))

if item_no == 1:
    print("Your order for Mandhi has arrived")
elif item_no == 2:
    print("Your order for KFC has arrived")
elif item_no == 3:
    print("Your order for Biriyani has arrived")
elif item_no == 4:
    print("Your order for Meals has arrived")
elif item_no == 5:
    print("Your order for Ice Cream has arrived")
else:
    print("Wrong placement of order")
