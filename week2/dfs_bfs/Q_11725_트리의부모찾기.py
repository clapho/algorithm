import sys
sys.setrecursionlimit(10 ** 7)

def input_():
    return sys.stdin.readline().rstrip()

N = int(input_())
parents = [0] * (N + 1)
visited = [False] * (N + 1)
tree = [[] for _ in range(N + 1)]

for i in range(N - 1):
    src, dest = map(int, input_().split(" "))
    tree[src].append(dest)
    tree[dest].append(src)

def dfs(node):
    visited[node] = True

    for i in tree[node]:
        if not visited[i]:
            parents[i] = node
            dfs(i)

dfs(1)
for i in range(2, N + 1):
    print(parents[i])
