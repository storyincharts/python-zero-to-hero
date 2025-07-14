m  = int(input("Enter the marks:"))
s  = int(input("Enter the marks:"))
e  = int(input("Enter the marks:"))

total = m + s + e
average = total / 3

percetage = (total /300)*100
grade = ""
if percetage > 90:
    grade = "A"
elif percetage >75 and percetage<=90:
    grade = "B"
elif percetage >45 and percetage<=75:
    grade = "C"
else:
    grade = "F"

print(f"Total marks: {total}\nAverage: {average}\nGrade: {grade}")
   