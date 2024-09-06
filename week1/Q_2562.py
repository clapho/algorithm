nums = [int(input()) for _ in range(9)]

maxValue = -1
maxIndex = 0

for i in range(9):
    if nums[i] > maxValue:
        maxValue = nums[i]
        maxIndex = i

print(maxValue)
print(maxIndex + 1)
