n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    

# DFS 구현
def DFS(x,y):
    if x < 0 or y < 0 or x > n-1 or y > n-1:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        DFS(x-1,y)
        DFS(x,y-1)
        DFS(x+1,y)
        DFS(x,y+1)
        return True
    return False

# 카운터 초기화
counter = 0;

# 모든 노드에 대하여 DFS 수행
for i in range(n):
    for j in range(m):
        if DFS(i,j) == True:
            counter += 1
        else:
            print("벽을 만났습니다 \n");

print(counter)
