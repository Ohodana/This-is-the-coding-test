import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
#TODO Q.34다시 풀기
def Biary_search_lower(array, x):
    returnValue = bisect_left(array, x)
    return returnValue
    

n = int(input())
array = [0].append(list(map(int, input().split())))

# n = 7
# array =  [0, 15, 11, 4, 8, 5, 2, 4]

d = [0, 1] 
x = [0, array[1]]

for i in range(2, n + 1):
    sc = Biary_search_lower(x, array[i])
    if sc == len(x):
        x.append(array[i])
        d.append(d[i-1]+1)
    else:
        x[sc] = min(x[sc], array[i])
        d.append(sc)
    
print(max(d))