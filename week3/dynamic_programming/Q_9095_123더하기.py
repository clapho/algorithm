import sys

def input_():
    return sys.stdin.readline().rstrip()

T = int(input_())

d = [0] * 12
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, 12):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

for _ in range(T):
    N = int(input_())

    print(d[N])
