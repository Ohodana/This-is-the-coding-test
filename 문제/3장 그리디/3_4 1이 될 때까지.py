# N, K = map(int, input().split())

N, K = 110, 9
returnValue = 0

while True:
    tmp = (N // K) * K
    returnValue += (N - tmp)
    N = tmp
    
    if N < K:
        break;
    
    returnValue += 1
    N //= K
    
returnValue += (N - 1)
print(returnValue)

