import sys
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]
check = [False for _ in range(N + 1)]

# 입력
for _ in range(N - 1):
    j, k = map(int, input().split())
    tree[j].append(k)
    tree[k].append(j)

def find(node_num):
    check[node_num] = True
    for child in tree[node_num]:
        if not check[child]:
            parents[child] = node_num
            find(child)

find(1)

for i in range(2, N + 1):
    print(parents[i])
