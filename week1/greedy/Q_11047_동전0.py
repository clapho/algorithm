import sys

def input_():
    return sys.stdin.readline().rstrip()

N, K = map(int, input_().split())
coins = []
coin_num = 0

for i in range(N):
    coins.append(int(input_()))

for i in range(N-1, -1, -1):
    if coins[i] > K:
        continue

    while K >= coins[i]:
        coin_num += K // coins[i]
        K = K % coins[i]

print(coin_num)
