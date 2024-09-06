T = int(input())

for _ in range(T):
    r, s = input().split(" ")
    R = int(r)
    S = list(s)

    result = ""
    for alp in S:
        result += alp * R

    print(result)
