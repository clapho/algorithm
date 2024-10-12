import sys

def input_():
    return sys.stdin.readline().rstrip()

str1 = [""] + list(input())
str2 = [""] + list(input())

d = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

print(d[len(str1)-1][len(str2)-1])
