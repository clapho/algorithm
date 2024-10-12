import sys

def input_():
    return sys.stdin.readline().rstrip()

N = int(input())
score = [0] * (N + 3)
d = [[0 for _ in range(N + 3)] for _ in range(3)]

for i in range(1, N + 1):
    score[i] = int(input_())

d[1][1] = score[1]
d[1][2] = score[2]
d[2][1] = 0
d[2][2] = score[1] + score[2]


for i in range(3, N + 1):
    d[1][i] = max(d[1][i - 2], d[2][i - 2]) + score[i]
    d[2][i] = d[1][i - 1] + score[i]

print(max(d[1][N], d[2][N]))
