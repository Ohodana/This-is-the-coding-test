#Q.03 문자열 뒤집기
# 이 문제는 문자열 1, 0 의 수를 세고 (연결된 수는 하나로 판별) 적은 것을 출력하면 되는 문제이다.

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = list(map(int, input.split()))
    
    n0 = n1 = 0
    counter = -1
    
    if n[0] == 0:
        n0 += 1
        count = 0
    else:
        n1 += 1
        count = 1
    
    for i in range(1, len(n) - 1):
        if n[i] == 0 and count == 1:
            n0 += 1
            count = 0
        elif n[i] == 1 and count == 0:
            n1 += 1
            count = 1
    print(min(n0, n1))