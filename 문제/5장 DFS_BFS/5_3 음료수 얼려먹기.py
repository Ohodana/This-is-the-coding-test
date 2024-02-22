n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    

# DFS ����
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

# ī���� �ʱ�ȭ
counter = 0;

# ��� ��忡 ���Ͽ� DFS ����
for i in range(n):
    for j in range(m):
        if DFS(i,j) == True:
            counter += 1
        else:
            print("���� �������ϴ� \n");

print(counter)
