import sys

def input_():
    return sys.stdin.readline().rstrip()

N = int(input())

wine = [0 for _ in range(N + 1)]
d = [[0 for _ in range(N + 1)] for _ in range(3)]

for i in range(1, N + 1):
    wine[i] = int(input_())

d[0][1] = 0
d[1][1] = wine[1]
d[2][1] = wine[1]

for i in range(2, N + 1):
    d[0][i] = max(d[0][i - 1], max(d[1][i - 1], d[2][i - 1]))
    d[1][i] = d[0][i - 1] + wine[i]
    d[2][i] = d[1][i - 1] + wine[i]

print(max(d[0][N], max(d[1][N], d[2][N])))
