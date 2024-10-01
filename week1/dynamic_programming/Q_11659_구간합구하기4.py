import sys

def input_():
    return sys.stdin.readline().rstrip()

N, M = map(int, input_().split())

nums = list(map(int, input_().split()))
nums = [0] + nums

results = []
prefix = [0] * (N + 1)

prefix[1] = nums[1]
for idx in range(2, N + 1):
    prefix[idx] = prefix[idx - 1] + nums[idx]

for _ in range(M):
    i, j = map(int, input_().split())

    results.append(prefix[j] - prefix[i - 1])

for result in results:
    print(result)
