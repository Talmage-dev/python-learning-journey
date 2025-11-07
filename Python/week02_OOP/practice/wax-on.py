price = 19.99
quantity = 3
tax_rate = 0.08

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Total: ${total:.2f}")