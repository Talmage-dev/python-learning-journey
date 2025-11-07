""" Day 9 Practice Set: Real-World Module Usage """

# # Practice 1: Date and Time Operations

# from datetime import datetime

# now = datetime.now()
# formatted = now.strftime("%Y-%m-%d %H:%M:%S")

# print(formatted)

# # Practice 2: Working wi JSON

# import json

# student = {"name": "Alice", "age": 25, "grades": [85, 90, 92]}
# json_string = json.dumps(student)

# print(json_string)

# # Practice 3: File Operations with OS Module

# import os

# current_dir = os.getcwd()
# files = os.listdir(".")
# exists = os.path.exists("test.txt")

# print(f"Current directory: {current_dir}")
# print(f"Files: {files}")
# print(f"test.txt exists: {exists}")

# # Practice 4: Random Data Genereation

# import random

# numbers = [random.randint(1, 100) for _ in range(5)]
# names = ["Alice", "Bob", "Charlie","Diana"]
# chosen_name = random.choice(names)

# print(f"Random numbers: {numbers}")
# print(f"Chosen name: {chosen_name}")

# Practice 5: Combining Multiple Modules

import json
import datetime as dt
import random

now = dt.datetime.now()
timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
names = ["Kardia", "Talmage", "Boyd", "Jaimee", "Steven"]
user = random.choice(names)
status = ["login", "logout"]
action =  random.choice(status)
score = random.randint(1, 100)

log_entry = {"timestamp": timestamp, "user": user, "action": action, "score": score}

log = json.dumps(log_entry)
with open("log.json", "w") as f:
    json.dump(log_entry, f)
print(json.dumps(log_entry))