import sys
import heapq

def input_():
    return sys.stdin.readline().rstrip()

N = int(input_())
M = int(input_())
graph = [[] for _ in range(N + 1)]

min_cost = 0

for i in range(M):
    u, v, cost = map(int, input_().split(" "))
    graph[u].append([v, cost])

src, dest = map(int, input_().split(" "))
costs = [1e9 for _ in range(N + 1)]
costs[src] = 0
heap = []
heapq.heappush(heap, [0, src])

while heap:
    cur_cost, cur_v = heapq.heappop(heap)

    if costs[cur_v] < cur_cost:
        continue

    for next_v, next_cost in graph[cur_v]:
        sum_cost = cur_cost + next_cost
        if sum_cost >= costs[next_v]:
            continue

        costs[next_v] = sum_cost
        heapq.heappush(heap, [sum_cost, next_v])

print(costs[dest])
