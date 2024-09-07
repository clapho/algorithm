N = int(input())

set_arr = set([input() for _ in range(N)])

arr = list(set_arr)

result = sorted(arr, key = lambda x : (len(x), x))

for i in range(len(arr)):
    print(result[i])