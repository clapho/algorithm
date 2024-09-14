import sys

def input_():
    return sys.stdin.readline().rstrip()

N, M = map(int, input_().split(" "))
numbers = list(map(int, input_().split(" ")))
numbers.sort()
output = []

def perm(depth, start):
    if depth == M:
        for i in range(M):
            print(output[i], end = " ")
        print()
        return

    for i in range(start, N):
        output.append(numbers[i])
        perm(depth + 1, i)
        output.pop()

perm(0, 0)
