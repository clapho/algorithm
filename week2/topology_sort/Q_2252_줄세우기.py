import sys
from collections import deque

def input_():
    return sys.stdin.readline().rstrip()

N, M = map(int, input_().split(" "))

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for i in range(M):
    A, B = map(int, input_().split(" "))
    graph[A].append(B)
    indegree[B] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for v in graph[now]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    for res in result:
        print(res, end=" ")

topology_sort()
