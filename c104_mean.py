import csv
from collections import Counter
with open('HeightWeight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_list = []
for i in  range (len(file_data)):
    num= file_data[i][1]
    new_list.append(float(num))

n = len(new_list)
print(n)
sum = 0
for i in new_list:
    sum = sum + i

mean = sum / n

print("mean is :" + str(mean))



    
    



