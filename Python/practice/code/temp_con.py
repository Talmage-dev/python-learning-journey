""" Exercise 2: Temperature Converter (Intermediate) """

# Write a program that converts temperature from Celsius to Fahrenheit:
# 1) Create a variable celsius and set it to any temperature (e.g. 25)
# 2) Use the formula: fahrenheit = (celsius * 9/5) + 32
# 3) Print both temperatures with a descriptive message
# 4) Bonus: Round the Fahrenheit result to 1 decimal place using round(number, 1)

celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {round(fahrenheit, 1)}°F")