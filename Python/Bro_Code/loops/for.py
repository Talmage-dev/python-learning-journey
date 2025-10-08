# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# Count to ten
for x in range(1, 11):
    print(x)

#Count back from ten
for y in reversed(range(1, 11)):
    print(y)

#count to 10 but every second number
for a in range(0, 11, 2):
    print(a)

#in a string
credit_card = "1234-5678-9021-3456"

for i in credit_card:
    print(i)

#continue key word (skip)
for b in range(1, 21):
    if b == 13:
        continue
    else:
        print(b)

#break out of a loop
for c in range(1, 21):
    if c == 13:
        break
    else:
        print(c)
