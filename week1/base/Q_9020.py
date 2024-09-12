import math

def get_prime_numbers(number):
    prime_numbers = []
    arr = [True for _ in range(number + 1)]

    for i in range(2, int(math.sqrt(number)) + 1):
        if arr[i]:
            j = 2
            while i * j < number + 1:
                arr[i * j] = False
                j += 1

    for i in range(2, number + 1):
        if arr[i]:
            prime_numbers.append(i)

    return prime_numbers

T = int(input())
nums = [int(input()) for i in range(T)]

for num in nums:
    prime_nums = get_prime_numbers(num)
    best_partition = (0, num)

    for prime in prime_nums:
        if prime > num // 2:
            break
        if (num - prime) in prime_nums:
            best_partition = (prime, num - prime)

    print(best_partition[0], best_partition[1])
