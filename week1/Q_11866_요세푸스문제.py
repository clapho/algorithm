import sys
from collections import deque

sys.stdin = open("z_input.text", "r")

def input_():
    return sys.stdin.readline().rstrip()

N, K = map(int, input_().split(" "))

q = deque()

result = []

for i in range(1, N + 1):
    q.append(i)

print("<", end="")

cnt = 0
while q:
    value = q.popleft()
    cnt += 1

    if cnt % K == 0:
        if not q:
            print(value, end="")
        else:
            print(value, end=", ")
    else:
        q.append(value)
print(">", end="")
