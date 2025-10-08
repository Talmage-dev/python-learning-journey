def fizzbuzz(n):

    for i in range(1, n + 1):
        if i % 15 == 0:
            yield"FizzBuzz"
        elif i % 3 == 0:
            yield"Fizz"
        elif i % 5 == 0:
            yield"Buzz"
        else:
            yield str(i)