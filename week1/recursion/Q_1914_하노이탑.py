import sys

sys.stdin = open("../z_input.text", "r")


def input_():
    return sys.stdin.readline().rstrip()

# 총 이동 횟수를 기록하는 변수
move_count = 0


# 이동 과정을 기록하기 위한 함수
def move(no, from_peg, to_peg):
    global move_count
    if no > 1:
        # 1단계: no-1개의 원판을 중간 장대로 옮기기
        move(no - 1, from_peg, 6 - from_peg - to_peg)

    # 2단계: 가장 큰 원판을 목적지로 이동
    move_count += 1
    if N <= 20:  # N이 20 이하인 경우에만 과정을 출력
        print(from_peg, to_peg)

    if no > 1:
        # 3단계: 중간 장대에 있는 no-1개의 원판을 목적지로 이동
        move(no - 1, 6 - from_peg - to_peg, to_peg)


# 입력 처리
N = int(input_())

# 1. 이동 횟수는 하노이의 탑에서 2^N - 1 입니다.
total_moves = (1 << N) - 1  # 2^N - 1 을 비트연산으로 계산

# 2. 첫 번째 줄에 이동 횟수를 출력
print(total_moves)

# 3. N이 20 이하일 때만 이동 과정을 출력
if N <= 20:
    move(N, 1, 3)
