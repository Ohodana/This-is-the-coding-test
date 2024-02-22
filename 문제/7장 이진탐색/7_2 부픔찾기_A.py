#이진 탐색을 이용하여 문제를 푸는 경우

def binary_search(array, target, start, end):
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    
n = int(input())
arrayA = list(map(int, input().split()))

m = int(input())
arrayB = list(map(int, input().split()))


for i in range(m):
    result = binary_search(arrayA, arrayB[i], 0, n-1)
    if arrayA[result] != arrayB[i]:
        print('no', end=' ')
    else:
        print('yes', end=' ')
        