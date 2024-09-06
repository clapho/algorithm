N = int(input())
nums = map(int, input().split(" "))

result = 0
for num in nums:
    if num == 1:
        continue

    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False

    if flag:
        result += 1

print(result)