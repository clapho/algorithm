import heapq
import sys

sys.stdin = open("z_input.text", "r")

def input_():
    return sys.stdin.readline().rstrip()

N = int(input_())

heap = []
for i in range(N):
    value = int(input_())
    if value == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-value, value))
