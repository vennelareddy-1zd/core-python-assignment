def calculate_average(marks):
    return sum(marks) / len(marks)

students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

averages = {}

for student, marks in students.items():
    averages[student] = round(calculate_average(marks), 2)

top_performer = max(averages, key=averages.get)

print("Average Marks:", averages)
print("Top Performer:", top_performer)
