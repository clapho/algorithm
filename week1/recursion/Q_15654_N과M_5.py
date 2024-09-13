N, M = map(int, input().split(" "))

numbers = list(map(int, input().split(" ")))
numbers.sort()
check = [False for _ in range(N)]
output = [0 for i in range(M)]

def perm(depth):
    if depth == M:
        for i in range(M):
            print(output[i], end=" ")
        print()
        return

    for i in range(N):
        if not check[i]:
            check[i] = True
            output[depth] = numbers[i]
            perm(depth + 1)
            check[i] = False

perm(0)
