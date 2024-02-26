#Q.01 모험가 길드

import sys
input = sys.stdin.readline

def guild(n, array):
    array.sort()
    returnValue = 0
    counter = 0
    
    for i in range(n):
        tmp = array[i]
        counter += 1
        if counter >= tmp:
            returnValue += 1
            counter = 0
    return returnValue


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    print(guild(n, array))