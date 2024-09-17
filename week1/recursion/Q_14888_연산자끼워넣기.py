import sys
N = int(input())

operand = list(map(int, input().split(" ")))
operators = list(map(int, input().split(" ")))

max_ans = -sys.maxsize + 1
min_ans = sys.maxsize

def sol(index, result):
    global max_ans
    global min_ans

    # base case
    if index == N:
        max_ans = max(max_ans, result)
        min_ans = min(min_ans, result)
        return

    # recursive case
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1

            if i == 0:
                sol(index + 1, result + operand[index])
            elif i == 1:
                sol(index + 1, result - operand[index])
            elif i == 2:
                sol(index + 1, result * operand[index])
            elif i == 3:
                # C++ 기준 음수의 나눗셈
                sol(index + 1, int(result / operand[index]))

            operators[i] += 1
sol(1, operand[0])

print(max_ans)
print(min_ans)
