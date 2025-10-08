# logical operators = evaluate multiple conditions (or, and, not)
#                or = at least one condition must be True
#               and = both conditions must be True
#               not = inverts the condition (not False, not True)

# Example 1 (or)
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is still scheduled")

# Example 2 (and, not)

temp2 = 30
is_sunny = False

if temp2 >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp2 <= 0 and is_sunny:
    print("It is COLD outside")
    print("But it is SUNNY")
elif 28 > temp2 > 0 and is_sunny:
    print("It is WARM outside")
    print("And it is SUNNY")
elif temp2 >= 28 and not is_sunny:
    print("It is HOT outside")
    print("But it is CLOUDY")
elif temp2 <= 0 and not is_sunny:
    print("It is COLD outside")
    print("And it is CLOUDY")
elif 28 > temp2 > 0 and is_sunny:
    print("It is WARM outside")
    print("But it is CLOUDY")