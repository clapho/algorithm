import sys

def input_():
    return sys.stdin.readline().rstrip()

N = int(input_())
M = int(input_())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    u, v = map(int, input().split(" "))
    graph[u][v] = 1
    graph[v][u] = 1

cnt = 0
def dfs(node):
    global cnt

    visited[node] = True
    cnt += 1
    for i in range(N + 1):
        if not visited[i] and graph[node][i] == 1:
            dfs(i)

dfs(1)
print(cnt - 1)
