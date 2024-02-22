#N, M, K = map(int, input().split());
#data = list(map(int, input().split()))

#Test data
N, M, K = 5, 8, 3;
data = [2, 4, 5, 4, 6]

returnValue = 0;
loopValue = 0;

data.sort(reverse=0);

for i in range(M):
    if loopValue != K:
        returnValue += data[N - 1];
        loopValue += 1;
    else:
        returnValue += data[N - 2];
        loopValue = 0;

print(returnValue);