""" Day 7 Practice Exercise: Reading and processing CSV-like Files """

# 6

def save_employees_to_file(employees, filename):
    with open(filename, "w") as file:
        for key, info in employees.items():  #Extract values from dict
            name = info["name"]
            salary = info["salary"]

            # Create line with commas
            line = f"{key},{name},{salary}\n" 

            # Write to file
            file.write(line)