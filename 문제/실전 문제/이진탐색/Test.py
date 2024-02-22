import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def Biary_search_lower(array, x):
    returnValue = bisect_left(array, x)
    return returnValue
    
print(Biary_search_lower([1, 2, 3, 4, 9], 8))