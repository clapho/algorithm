import sys
from collections import deque

def input_():
    return sys.stdin.readline().rstrip()

R, C = map(int, input().split(" "))

graph = []
water_map = [[0 for _ in range(C)] for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
water_q = deque()
result = []

for i in range(R):
    row = list(input_())
    graph.append(row)

    for j in range(C):
        if graph[i][j] == "S":
            q.append((i, j, 1))
        if graph[i][j] == "*":
            water_q.append((i, j, 1))
        if graph[i][j] == "D":
            water_map[i][j] = sys.maxsize

def water_bfs():
    while water_q:
        x, y, depth= water_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue

            if water_map[nx][ny] == 0 and graph[nx][ny] != "X" and graph[nx][ny] != "D":
                water_map[nx][ny] = depth + 1
                water_q.append((nx, ny, depth + 1))


def bfs():
    global result

    while q:
        x, y, depth = q.popleft()

        if graph[x][y] == "D":
            result.append(depth - 1)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue

            if graph[nx][ny] != "X" and water_map[nx][ny] > depth + 1:
                q.append((nx, ny, depth + 1))


water_bfs()
bfs()

if result:
    print(max(result))
else:
    print("KAKTUS")
