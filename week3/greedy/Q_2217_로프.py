import sys

def input_():
    return sys.stdin.readline().rstrip()

N = int(input_())
rope = []
result = []

for i in range(N):
    rope.append(int(input_()))

rope.sort()

for i in range(N):
    result.append(rope[i] * (N - i))

print(max(result))
