import sys

sys.stdin = open("../z_input.text", "r")

def input_():
    return sys.stdin.readline().rstrip()

N, M = map(int, input_().split(' '))
trees = list(map(int, input_().split(' ')))

def sum_tree_heights(mid, tree_heights):
    result = 0
    for height in tree_heights:
        if height <= mid:
            continue
        else:
            result += (height - mid)
    return result

def binary_search(start, end):
    max_height = 0
    while start <= end:
        mid = (start + end) // 2
        total_sum = sum_tree_heights(mid, trees)

        if total_sum >= M:
            max_height = mid
            start = mid + 1
        else:
            end = mid - 1

    return max_height

max_tree_height = max(trees)
print(binary_search(0, max_tree_height))
