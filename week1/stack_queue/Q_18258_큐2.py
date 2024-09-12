import sys
from collections import deque

sys.stdin = open("../z_input.text", "r")

def input_():
    return sys.stdin.readline().rstrip()

N = int(input_())

def solution(command, q):

    method = command.split(" ")

    if method[0] == "push":
        q.append(method[1])
    elif method[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif method[0] == "size":
        print(len(q))
    elif method[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif method[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif method[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)

queue = deque()
for i in range(N):
    method = input_()
    solution(method, queue)
