import sys

input = sys.stdin.readline

n = int(input())
array = []


for _ in range(n):
    array.append(list(map(int, input().split())))

for j in range(1, n):
    for i in range(j + 1):
        if i == 0:
            left_up = 0
        else:
            left_up = array[j - 1][i - 1]
        if j == i:
            up = 0
        else:
            up = array[j - 1][i]
        
        array[j][i] = array[j][i] + max(left_up, up)

print(max(array[n - 1]))