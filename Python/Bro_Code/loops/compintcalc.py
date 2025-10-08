# Phython compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the amount you wish to invest: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("What is the interest rate: "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero")

while time <= 0:
    time = int(input("How long would you like to invest in years?: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

total = principle * pow((1 + rate / 100), time)

print(f"With an initial investment of ${principle}, and having invested it for {time} years at an interest rate of {rate}%, you will have ${total}.")