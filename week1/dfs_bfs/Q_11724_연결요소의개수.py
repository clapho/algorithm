import sys
sys.setrecursionlimit(10 ** 7)

def input_():
    return sys.stdin.readline().rstrip()

N, M = map(int, input_().split(" "))
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

for i in range(M):
    u, v = map(int, input_().split(" "))
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
