filename = "sample.txt"

try:
    print("Reading file content:\n")
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

