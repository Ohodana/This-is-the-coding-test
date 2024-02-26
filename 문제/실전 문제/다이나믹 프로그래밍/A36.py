#Q.36 편집 거리
# 이 문제는 편집 거리 알고리즘을 통해 풀수 있음. 
# 편집 거리 알고리즘은 두 문자열이 주어졌을 때, 문자열1을 문자열2로 바꾸기 위해 필요한 연산의 횟수를 구하는 알고리즘
# #TODO 다시 풀어보기
# 문제에 필요한 알고리즘 : https://hsp1116.tistory.com/41

import sys

def editLen(str1, str2):
    Len1 = len(str1)
    Len2 = len(str2)
    
    # DP 테이블 생성
    dp = [[0] * (Len2 + 1) for _ in range(Len1 + 1)]
    
    # DP 테이블 초기화
    for i in range(1, Len1 + 1):
        dp[i][0] = i
    for j in range(1, Len2 + 1):
        dp[0][j] = j
    
    # 최소 편집 거리 계산
    for i in range(1, Len1 + 1):
        for j in range(1, Len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
                
    print(dp[Len1][Len2])

if __name__ == "__main__":
    str1 = sys.stdin.readline().rstrip()
    str2 = sys.stdin.readline().rstrip()
    editLen(str1, str2)