import sys

def input_():
    return sys.stdin.readline().rstrip()

N = int(input_())
d = [[0 for _ in range(3)] for _ in range(N + 2)]

R = [0] * (N + 1)
G = [0] * (N + 1)
B = [0] * (N + 1)

for i in range(1, N + 1):
    r, g, b = map(int, input_().split())
    R[i] = r
    G[i] = g
    B[i] = b

#  d[i][0] = i번째 집까지 칠할 때 비용의 최솟값, i번째 집은 빨강
#  d[i][1] = i번째 집까지 칠할 때 비용의 최솟값, i번째 집은 초록
#  d[i][2] = i번째 집까지 칠할 때 비용의 최솟값, i번째 집은 파랑

d[1][0] = R[1]
d[1][1] = G[1]
d[1][2] = B[1]

for i in range(2, N + 1):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + R[i]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + G[i]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + B[i]

print(min(d[N][0], d[N][1], d[N][2]))
