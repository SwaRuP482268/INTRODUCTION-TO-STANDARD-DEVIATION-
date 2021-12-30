import math
import csv

with open("class2.csv",newline="")as f:
        reader = csv.reader(f)
        file_data = list(reader)

file_data.pop(0)
total_marks = 0
total_entries = len(file_data)

for marks in file_data:
        total_marks += float(marks[1])

mean = total_marks/total_entries

print("Mean (Average) is -> "+str(mean))

square_list = []
for number in file_data:
        a = int(number)-mean(file_data)
        a = a**2 
        square_list.append(a)

sum = 0

for i in square_list:
        sum = sum+i

result = sum/(len(file_data))
std_deviation = math.sqrt(result)

print(std_deviation)

