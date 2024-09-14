N, M = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))
numbers.sort()
output = []

def perm(depth):
    if depth == M:
        for i in range(M):
            print(output[i], end=" ")
        print()
        return

    for i in range(N):
        output.append(numbers[i])
        perm(depth + 1)
        output.pop()

perm(0)
