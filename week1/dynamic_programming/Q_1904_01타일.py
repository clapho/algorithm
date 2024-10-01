import sys

def input_():
    return sys.stdin.readline().rstrip()

N = int(input_())

d = [0] * (N + 3)
d[1] = 1
d[2] = 2

for i in range(3, N + 1):
    d[i] = (d[i - 1] + d[i - 2]) % 15746

print(d[N])
