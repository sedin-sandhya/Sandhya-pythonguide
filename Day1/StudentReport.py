marks = []
print("Enter the marks")
total = 0
count = 0
for i in range(1,6):
    a = int(input("Enter subject " + str(i) + " marks:"))
    marks.append(a)
    total += a
print("Total marks: ", total)
print("Percentage:", total/5)
for i in marks:
    if i >= 91 and i <= 100:
        print("mark: ", i, "grade: A")
    elif i >= 81 and i <= 90:
        print("mark: ", i, "grade: B")
    elif i >= 71 and i <= 80:
        print("mark: ", i, "grade: C")
    elif i >= 61 and i <= 70:
        print("mark: ", i, "grade: D")
    elif i >= 51 and i <= 60:
        print("mark: ", i, "grade: E")
    else:
        print("mark: ", i, "grade: F  Failed in this subject")
        count += 1
print("You have failed in", count, "subjects")
