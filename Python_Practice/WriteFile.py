# Writing to a file
with open("grades.txt", "w") as file:
    file.write("John: A\n")
    file.write("Emma: B\n")
    file.write("Liam: C\n")

print("Data written to grades.txt")
