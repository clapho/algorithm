import sys

sys.stdin = open("z_input.text", "r")

def input_():
    return sys.stdin.readline().rstrip()

N = int(input_())
arr = []
def solution(command, arr):
     method = command.split(" ")

     if method[0] == "push":
         arr.append(method[1])
     elif method[0] == "pop":
         if arr:
            print(arr.pop())
         else:
             print(-1)
     elif method[0] == "top":
         if arr:
             print(arr[-1])
         else:
             print(-1)
     elif method[0] == "size":
         print(len(arr))
     elif method[0] == "empty":
         if not arr:
             print(1)
         else:
             print(0)
     else:
         print()
for i in range(N):
    command = input_()
    solution(command, arr)
