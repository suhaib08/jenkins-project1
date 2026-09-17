# Student Management and Academic Performance System - report generator
students = [
    {"name": "Arun", "cgpa": 8.7},
    {"name": "Divya", "cgpa": 9.1},
    {"name": "Karthik", "cgpa": 7.4},
]

average = sum(s["cgpa"] for s in students) / len(students)

with open("report.txt", "w") as f:
    f.write("Academic Performance Report\n")
    f.write("Total Students: %d\n" % len(students))
    f.write("Average CGPA: %.2f\n" % average)
    for s in students:
        f.write("%s - %.2f\n" % (s["name"], s["cgpa"]))

print("Report generated.")
