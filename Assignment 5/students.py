students = int(input("Enter number of students: "))

percentages = []   

for s in range(1, students + 1):
    print(f"\nEnter marks for Student {s}:")
    total = 0
    
    for i in range(1, 6):   # 5 subjects
        marks = int(input(f"  Subject {i} marks: "))
        total += marks
    
    percentage = total / 5
    percentages.append(percentage)
    print(f"  Percentage of Student {s}: {percentage:.2f}%")

# Display all percentages
print("\nAll Students Percentages:")
for idx, p in enumerate(percentages, start=1):
    print(f"  Student {idx}: {p:.2f}%")

# Average percentage of class
avg_percentage = sum(percentages) / students
print(f"\nAverage Percentage of class: {avg_percentage:.2f}%")