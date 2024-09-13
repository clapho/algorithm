def fibo(n):
    if n == 1 or n == 2:
        return 1

    if cache[n] != 0:
        return cache[n]
    cache[n] = fibo(n - 1) + fibo(n - 2)
    return cache[n]

n = int(input())

cache = [0 for i in range(n + 1)]
result = fibo(n)
print(result)