from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

counter = 0;

def BFS():
    deque = deque()
    deque.append((0, 0))
    
    while True:
        if not deque:
            break
        x, y = deque.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                deque.append((nx,ny))
    return graph[n-1][m-1]

print(BFS())