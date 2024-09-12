import sys

sys.stdin = open("../z_input.text", "r")

def input_():
    return sys.stdin.readline().rstrip()

A, B, C = map(int, input_().split(" "))

def power(a, b):
    if b == 1:
        return a % C

    half = power(a, b // 2)

    if b % 2 == 0:
        return (half * half) % C
    else:
        return (((half * half) % C) * a) % C

print(power(A, B))