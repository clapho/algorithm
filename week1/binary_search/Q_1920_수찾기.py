from sys import stdin

def input_():
    return stdin.readline().rstrip()

N = int(input_())
A = list(map(int, input_().split(' ')))
M = int(input_())
B = list(map(int, input_(). split(' ')))

A.sort()

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for val in B:
    print(binary_search(val, A))
