arr = [int(input()) for i in range(9)]
total = sum(arr)
idx1 = -1
idx2 = -1

arr.sort()
for i in range(8):
    flag = True
    for j in range(i + 1, 9):
        if total - arr[i] - arr[j] == 100:
           idx1 = i
           idx2 = j
           flag = False
           break

    if not flag:
        break

for i in range(len(arr)):
    if i == idx1 or i == idx2:
        continue
    print(arr[i])
