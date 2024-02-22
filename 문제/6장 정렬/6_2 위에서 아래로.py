
# °³ Á¿¹ä ¹®Á¦
n = int(input());

array = [];
for i in range(n):
    array.append(input());
    
array.sort(reverse=True);

for i in range(n):
    print(array[i], end=' ');