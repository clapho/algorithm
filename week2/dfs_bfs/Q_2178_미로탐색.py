from collections import deque

N, M = map(int, input().split(" "))

maze = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

for _ in range(N):
    row = list(map(int, input()))
    maze.append(row)

def bfs(x, y):
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))

    return maze[N - 1][M - 1]

print(bfs(0, 0))
