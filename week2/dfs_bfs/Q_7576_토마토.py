import sys
from collections import deque

def input_():
    return sys.stdin.readline().rstrip()

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if distance[nx][ny] == 0 and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1

M, N = map(int, input_().split(" "))
graph = []
distance = [[0 for _ in range(M)] for _ in range(N)]
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    row = list(map(int, input_().split(" ")))
    graph.append(row)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))

bfs()

flag = False
max_value = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            flag = True
        max_value = max(max_value, distance[i][j])

if flag:
    print(-1)
else:
    print(max_value)
