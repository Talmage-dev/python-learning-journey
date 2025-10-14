""" Day 7 Practice Exercise: Reading and processing CSV-like Files """

# 2

def load_data_from_file(filename):
    data = {} # Empty dict to store results

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")     # Split by comma
            car_num = parts[0]      # 1st item
            model = parts[1]   # 2nd item
            price = int(parts[2])   # 3rd item
            data[car_num] = {"model": model, "price": price}
    return data