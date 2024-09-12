import sys
import heapq

sys.stdin = open("../z_input.text", "r")

def input_():
    return sys.stdin.readline().rstrip()

N = int(input_())

max_heap = []
min_heap = []

for i in range(N):
    value = int(input_())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -value)
    else:
        heapq.heappush(min_heap, value)

    if not min_heap:
        print(-max_heap[0])
        continue

    if -max_heap[0] > min_heap[0]:
        b = -heapq.heappop(max_heap)
        s = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -s)
        heapq.heappush(min_heap, b)

    print(-max_heap[0])