""" Day 9: Modules and Imports """

# Final Challenge: Build a Utility Module

from modules import file_utils as fu

# 1. Create a test file with some content
write = fu.write_file_safe("test.txt", "Hello, World!")

# 2. Reads it back
content = fu.read_file_safe("test.txt")

# 3. Counts the lines
count = fu.count_lines("test.txt")

# 4. Checks if it exists
check = fu.file_exists("test.txt")

# 5. Print results
print(write)
print(content)
print(count)
print(check)