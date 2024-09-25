import sys
from collections import deque

def input_():
    return sys.stdin.readline().rstrip()

n = int(input_())
m = int(input_())

graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
result = 0

q = deque()

for i in range(m):
    a, b = map(int, input_().split(" "))
    graph[a].append(b)
    graph[b].append(a)

def bfs(node):
    q.append(node)
    visited[node] = 1

    while len(q) > 0:
        now = q.popleft()

        for friend in graph[now]:
            if visited[friend] == 0:
                q.append(friend)
                visited[friend] = visited[now] + 1


bfs(1)
for i in range(2, n + 1):
    if 0 < visited[i] <= 3:
        result += 1

print(result)
