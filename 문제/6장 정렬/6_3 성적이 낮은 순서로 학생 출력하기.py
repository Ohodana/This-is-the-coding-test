
n = int(input());

array = []
for i in range(n):
    tmp = input().split();
    array.append((tmp[0], tmp[1]));
    
array.sort(key=lambda student: student[1]);

for student in array:
    print(student[0], end=' ');