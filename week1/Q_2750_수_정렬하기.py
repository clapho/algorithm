N = int(input())
nums = [int(input()) for i in range(N)]

nums.sort()

for i in range(N):
    print(nums[i])
