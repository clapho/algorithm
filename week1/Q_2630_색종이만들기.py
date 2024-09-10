import sys

sys.stdin = open("z_input.text", "r")

def input_():
    return sys.stdin.readline().rstrip()

N = int(input_())
blue_count = 0
white_count = 0

def flip(start_x, start_y, n):
    global white_count, blue_count

    start = whole_map[start_x][start_y]
    flag = True

    for i in range(start_x, start_x + n):
        for j in range(start_y, start_y + n):
            if whole_map[i][j] != start:
                flag = False
                break
        if not flag:

            break
    if flag:
        if start == 0:
            white_count += 1
        else:
            blue_count += 1
    else:
        flip(start_x, start_y, n // 2)
        flip(start_x + n // 2, start_y, n // 2)
        flip(start_x, start_y + n // 2, n // 2)
        flip(start_x + n // 2, start_y + n // 2, n // 2)


whole_map = []
for i in range(N):
    line = list(map(int, input_().split(" ")))
    whole_map.append(line)

flip(0, 0, N)

print(white_count)
print(blue_count)
