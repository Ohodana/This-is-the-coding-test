#N, M, K = map(int, input().split());
#data = list(map(int, input().split()))

#Test data
N, M, K = 5, 8, 3;
data = [2, 4, 5, 4, 6]

data.sort(reverse=0)

counter = int(M / (K + 1)) * K
counter += M % (K + 1)

returnValue = 0
returnValue += data[N - 1] * counter
returnValue += data[N - 2] * (M - counter)

print(returnValue)
