import csv

# Assuming 'data.csv' has columns: Name, Marks
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    marks = [int(row['Marks']) for row in reader]

average = sum(marks) / len(marks)
print(f"Average Marks: {average}")