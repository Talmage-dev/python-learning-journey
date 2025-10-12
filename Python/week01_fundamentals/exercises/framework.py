""" Day 5 Practice Exercise: Apply Framework """

# Problem: Grade Statistics Calculator

# Variables:
scores = [85, 92, 78, 90,88]

# Functions:

# Function: get_highest_score
# Input: list of scores
# Output: highest score (int)
# Steps: Return maximum value from list
def get_highest_score(scores):
    return max(scores)

# Function: get_lowest_score
# Input: list of scores
# Output: lowest score (int)
# Steps: Return minimum value from list
def get_lowest_score(scores):
    return min(scores)

# Function: get_average_score
# Input: list of scores
# Output: average score (float)
# Steps:
#   1. Sum all scores
#   2. Divide by count of scores
#   3. Return result
def get_average_score(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

# Function: count_above_85
# Input: list of scores
# Output: count (int)
# Steps:
#   1. Initialize counter to 0
#   2. Loop through each score
#   3. If score > 85, increment counter
#   4. Return counter
def count_above_85(scores):
    count = 0
    for score in scores:
        if score > 85:
            count += 1
    return count

# Function: is_passing
# Input: average score (float)
# Output: message (string)
# Steps:
#   1. If average >= 80, return "Pass"
#   2. Else return "Fail"
def is_passing(average):
    if average >= 80:
        return "Pass"
    else:
        return "Fail"
    
# Main Logic

# Calculate highest score
high = get_highest_score(scores)
# Calculate lowest score
low = get_lowest_score(scores)
# Calculate average score
ave = get_average_score(scores)
# Count scores above 85
count = count_above_85(scores)
# Determaine pass/fail based on average
result = is_passing(ave)
# Display all results
print(f"Highest score: {high}")
print(f"Lowest score: {low}")
print(f"Average score: {ave}")
print(f"Number of scores above 85: {count}")
print(f"Average result: {result}")