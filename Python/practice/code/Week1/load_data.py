""" Day 7 Practice Exercise: Reading and processing CSV-like Files """

def load_data_from_file(filename):
    data = {} # Empty dict to store results

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")     # Split by comma
            id_num = parts[0]      # 1st item
            name = parts[1]   # 2nd item
            price = float(parts[2])   # 3rd item
            data[id_num] = {"name": name, "price": price}
    return data