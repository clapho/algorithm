N = int(input())
memo = [0] * (N + 1)

def fibo(n):
    if n == 1 or n == 2:
        return 1

    if memo[n] != 0:
        return memo[n]

    memo[n] = fibo(n - 1) + fibo(n - 2)

    return memo[n]

print(fibo(N))
