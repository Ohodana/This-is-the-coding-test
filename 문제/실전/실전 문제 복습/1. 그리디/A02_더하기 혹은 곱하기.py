#Q.02 더하기 혹은 곱하기

import sys
input = sys.stdin.readline

def plusOrMul(n, array):
    returnValue = 0
    for i in range(n):
        if returnValue == 0 or returnValue == 1:
            returnValue += array[i]
        else:
            returnValue *= array[i]
    return returnValue


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().rstrip()))
    print(plusOrMul(n, array))