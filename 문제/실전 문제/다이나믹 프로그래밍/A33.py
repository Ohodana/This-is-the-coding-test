import sys
input = sys.stdin.readline

array = []
t = int(input())
max_value = 0
dp = [0 for _ in range(t + 1)] 

array = []
for i in range(t):
    array.append(list(map(int, input().split())))

for i in range(t - 1, -1, -1):
    time = array[i][0] + i
    if t >= time:
        dp[i] = max(array[i][1] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
    
print(max_value)