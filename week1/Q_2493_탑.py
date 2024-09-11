import sys
from collections import deque

sys.stdin = open("z_input.text", "r")

def input_():
    return sys.stdin.readline().rstrip()

N = int(input_())

line = list(map(int, input_().split(" ")))

stack = deque()
result = [0 for i in range(N)]

for i in range(N):
    while stack and stack[-1][1] < line[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1][0] + 1

    stack.append((i, line[i]))

for i in range(N):
    print(result[i], end=" ")
