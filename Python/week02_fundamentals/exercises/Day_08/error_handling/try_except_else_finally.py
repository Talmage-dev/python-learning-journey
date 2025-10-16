""" Day 8 Error Handling """

# Practice Exercise 5: Safe File Writer

def write_data_safe(filename, data):
    try:
        with open(filename, "w") as file:
            file.write(data)
    except PermissionError:
        print("Error: Can't write to file")
        return None
    else:
        print("Write successful!")
    finally:
        print("Write operation complete")