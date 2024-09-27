N = int(input())

d = [0] * (N + 2)
d[1] = 1
d[2] = 3

for i in range(3, N + 1):
    d[i] = d[i - 2] + d[i - 2] + d[i - 1]

print(d[N] % 10007)
