price = int(input("Price of the shirt: "))
quan = int(input("Quantity of the Shirt: "))

total  = price * quan
print("Total Price: ", total)

discount = total * .20
print("Discount: ", discount) 

dp = total - discount
print("Discounted Price: ", dp)

cash = int(input("Cash: "))
change = cash - dp
print("Change: ", change)

print("Thanks for purchasing.")