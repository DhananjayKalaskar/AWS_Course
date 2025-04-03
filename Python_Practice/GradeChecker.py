def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Taking input from the user
score = int(input("Enter the score: "))
grade = check_grade(score)
print(f"Grade: {grade}")
