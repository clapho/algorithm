import sys

N = int(input())
W = []
answer = sys.maxsize
visited = [False for i in range(N)]

def search(start, node, cost, cnt):
    global answer
    if cnt == N and start == node:
        answer = min(answer, cost)
        return

    for j in range(N):
        if not visited[j] and W[node][j] != 0:
            visited[j] = True
            search(start, j, cost + W[node][j], cnt + 1)
            visited[j] = False

for i in range(N):
    temp = list(map(int, input().split(' ')))
    W.append(temp)

search(0, 0, 0, 0)

print(answer)


