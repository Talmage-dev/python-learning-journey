def read_file_safe(filename):
    """Read file with error handling. Returns content or None."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None

def write_file_safe(filename, content):
    """Write to file with error handling. Returns True/False."""
    try:
        with open(filename, "w") as file:
            file.write(content)
        return True
    except PermissionError:
        print(f"Error: Cannot write to {filename}")
        return False

def count_lines(filename):
    """Count lines in a file. Returns count or 0."""
    content = read_file_safe(filename)
    if content:
        return len(content.split("\n"))
    return 0

def file_exists(filename):
    """Check if file exists. Returns True/False."""
    import os
    return os.path.exists(filename)