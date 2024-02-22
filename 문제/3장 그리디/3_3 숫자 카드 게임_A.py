N, M = 2, 4

Line = [[7, 3, 1, 8], [3, 3, 3, 4]]

minValue = -1;

for i in range(N):
    tmpValue = min(Line[i])
    
    minValue = max(minValue, tmpValue)

print(minValue);

