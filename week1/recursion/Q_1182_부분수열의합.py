N, S = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
cnt = 0

def sol(index, sum_):
    global cnt

    if index == len(nums):
        return
    if sum_ + nums[index] == S:
        cnt += 1

    sol(index + 1, sum_ + nums[index])
    sol(index + 1, sum_)

sol(0, 0)
print(cnt)