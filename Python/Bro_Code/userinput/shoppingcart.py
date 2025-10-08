# Excercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is it's price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} {item}'s")
print(f"That will be ${total}")
