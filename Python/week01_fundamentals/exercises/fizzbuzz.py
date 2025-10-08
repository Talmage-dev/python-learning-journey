# First exercise, FIZZBUZZ function

# Rules:    -Numbers divisible by 3: return "Fizz"
#           -Numbers divisible by 5: return "Buzz"
#           -Numbers divisible by both return "FizzBuzz"
#           -Otherwise: return the number as a string.

def fizzbuzz(n):

    result = []

    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result