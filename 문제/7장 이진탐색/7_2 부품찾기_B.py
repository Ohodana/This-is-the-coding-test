#계수 정렬을 이용한 방법

n = int(input())
arrayA = list(map(int, input().split()))

m = int(input())
arrayB = list(map(int, input().split()))

arrayTmp = [0] * 1000001

for i in range(n):
    arrayTmp[arrayA[i]] = 1

for i in range(m):
    if arrayTmp[arrayB[i]] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
    