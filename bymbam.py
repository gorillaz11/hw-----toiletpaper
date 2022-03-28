product_name="toilet price"
product_price=5.0
delivery_cost=50
print("###############")
print(product_name,":",product_price)

answer=input("do you want to buy?")

if answer == "yes".lower() or "y".lower():
    order_quantity=int(input("how many?"))
    order_cost=order_quantity*product_price

    print("----------")
    print("order info")
    print(product_name,"x",order_quantity,"=",order_cost)
    
    answer=input("do you want delivery? ")
    if answer=="yes":
        order_cost+=delivery_cost
        print("order cost (including delivery)",order_cost)
else:
    print("too bad:(")