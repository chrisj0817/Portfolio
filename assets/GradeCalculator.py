percentage = int(input("Percentage on test: "))

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

if str(percentage).startswith(('8', '11', '18')) or percentage == 89:
    article = "An"
else:
    article = "A"

print(f"{article} {percentage} earned you a {grade}!")
