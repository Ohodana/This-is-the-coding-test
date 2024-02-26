#Q.35 못생긴수
import sys

def uglyNumSearch():
    
    input = sys.stdin.readline
    n = int(input())
    
    # 값들을 저장할 리스트(DP) 생성 및 변수 초기화
    uglyNum = [0 for _ in range(n)]
    uglyNum[0] = 1
    num1, num2, num3 = 2, 3, 5
    n2 = n3 = n5 = 0
    
    
    for i in range(n):
        
        uglyNum[i] = min(num1, num2, num3)
        
        if uglyNum[i] == num1:
            n2 += 1
            num1 = uglyNum[n2] * 2
        elif uglyNum[i] == num2:
            n3 += 1
            num2 = uglyNum[n3] * 3
        else:
            n5 += 1
            num3 = uglyNum[n5] * 5
    print(uglyNum[n-1])