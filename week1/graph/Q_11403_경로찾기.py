import sys

def input_():
    return sys.stdin.readline().rstrip()

N = int(input_())
G = []

for i in range(N):
    line = list(map(int, input_().split(" ")))
    G.append(line)

def dfs(node):
    for i in range(N):
        if not visited[i] and G[node][i] == 1:
            visited[i] = True
            dfs(i)

for i in range(N):
    visited = [False for _ in range(N)]
    dfs(i)
    for j in range(N):
        if visited[j]:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
