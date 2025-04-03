# Reading from a file
try:
    with open("grades.txt", "r") as file:
        content = file.read()
        print("File Content:\n", content)
except FileNotFoundError:
    print("File not found! Make sure to run the write program first.")
