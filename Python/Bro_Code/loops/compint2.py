# Phython compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the amount you wish to invest: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    rate = float(input("What is the interest rate: "))
    if rate < 0:
        print("Rate can't be less than zero")
    else:
        break

while True:
    time = int(input("How long would you like to invest in years?: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)

print(f"With an initial investment of ${principle}, and having invested it for {time} years at an interest rate of {rate}%, you will have ${total}.")