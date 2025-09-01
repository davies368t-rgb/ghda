AC = float(input("enter actual cost of object: "))
SP = float(input("enter selling price of object: "))

profit = AC-SP

if profit>0:
    print("profit")
if profit<0:
    print("loss")