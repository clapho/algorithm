from collections import deque
import sys

def input_():
    return sys.stdin.readline().rstrip()

N, M, K, X = map(int, input_().split(" "))

road = [[] for _ in range(N + 1)]
q = deque([X])
distance = [-1] * (N + 1)
distance[X] = 0
result = []

for i in range(M):
    u, v = map(int, input_().split(" "))
    road[u].append(v)

def bfs(node):
    q.append(node)

    while q:
        now = q.popleft()

        for i in road[now]:
            if distance[i] == -1:
                distance[i] = distance[now] + 1
                q.append(i)

bfs(X)

for i in range(1, N + 1):
    if distance[i] == K:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)
