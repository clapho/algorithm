import sys
sys.setrecursionlimit(10**9)

def input_():
    return sys.stdin.readline().rstrip()

arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break

def sol(tree):
    if len(tree) == 0:
        return

    left = []
    right = []
    root = tree[0]

    for i in range(1, len(tree)):
        if tree[i] > root:
            left = tree[1:i]
            right = tree[i:]
            break
    else:
        left = tree[1:]

    sol(left)
    sol(right)
    print(root)

sol(arr)
