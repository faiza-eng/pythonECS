import string
print("Word length filter from file")
file_path = "sample.txt"
try:
    length = int(input("Enter the word length to filter: "))
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        # ... filtering logic ...