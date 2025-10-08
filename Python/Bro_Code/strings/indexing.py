# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) #display first character
print(credit_number[:4]) #display first 4 characters
print(credit_number[5:9]) #display the next 4 characters
print(credit_number[10:]) #display the last lot of characters
print(credit_number[-1]) #a negative index starts from the last character
print(credit_number[::2]) #display every 2nd character in a string

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

reverse_number = credit_number[::-1]
print(reverse_number)