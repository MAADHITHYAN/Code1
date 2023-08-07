filename = input("Enter the filename : ") with open(filename) as file:

text = file.read()

letter = input("Enter the character to be searched : ")

count = 0

for char in text:

if char == letter:

count += 1

print(letter, "appears ", count," times in file")