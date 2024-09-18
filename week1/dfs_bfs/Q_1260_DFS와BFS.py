from collections import deque

N, M, V = map(int, input().split(" "))
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
q = deque()

for i in range(M):
    src, dest = map(int, input().split(" "))
    graph[src][dest] = 1
    graph[dest][src] = 1

def dfs(node):
    visited[node] = True
    print(node, end=" ")
    for i in range(1, N + 1):
        if not visited[i] and graph[node][i] == 1:
            dfs(i)

def bfs(node):
    q.append(node)
    visited[node] = True

    while len(q) > 0:
        now = q.popleft()
        print(now, end=" ")
        for i in range(1, N + 1):
            if not visited[i] and graph[now][i] == 1:
                q.append(i)
                visited[i] = True

dfs(V)
print()
visited = [False for _ in range(N + 1)]
bfs(V)
