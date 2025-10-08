# format specifiers = {value:flags} fortmat a value based on what flagss are inserted
#
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

#decimal places
print(f"Price 1 is ${price1:.2f}")
print(f"Price 1 is ${price2:.2f}")
print(f"Price 1 is ${price3:.2f}")

#allocate space
print(f"Price 1 is ${price1:10}")
print(f"Price 1 is ${price2:10}")
print(f"Price 1 is ${price3:10}")

#zero pad
print(f"Price 1 is ${price1:010}")
print(f"Price 1 is ${price2:010}")
print(f"Price 1 is ${price3:010}")

#left justified
print(f"Price 1 is ${price1:<10}")
print(f"Price 1 is ${price2:<10}")
print(f"Price 1 is ${price3:<10}")

#right justified
print(f"Price 1 is ${price1:>10}")
print(f"Price 1 is ${price2:>10}")
print(f"Price 1 is ${price3:>10}")

#center align
print(f"Price 1 is ${price1:^10}")
print(f"Price 1 is ${price2:^10}")
print(f"Price 1 is ${price3:^10}")

#positive values
print(f"Price 1 is ${price1:+}")
print(f"Price 1 is ${price2:+}")
print(f"Price 1 is ${price3:+}")

#thousand seperator
print(f"Price 1 is ${price1:,}")
print(f"Price 1 is ${price2:,}")
print(f"Price 1 is ${price3:,}")

#combination of specifiers
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 1 is ${price2:+,.2f}")
print(f"Price 1 is ${price3:+,.2f}")