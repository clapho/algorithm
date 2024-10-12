import sys
sys.setrecursionlimit(10**6)
def input_():
    return sys.stdin.readline().rstrip()

def dfs(node, group):
    visited[node] = group

    for i in graph[node]:
        if not visited[i]:
            result = dfs(i, -group)
            if not result:
                return False
        else:
            if visited[i] == group:
                return False
    return True

K = int(input())

for i in range(K):
    V, E = map(int, input_().split(" "))
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)

    for j in range(E):
        u, v = map(int, input_().split(" "))
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V + 1):
        if not visited[i]:
            result = dfs(i, 1)
            if not result:
                break

    print("YES") if result else print("NO")
