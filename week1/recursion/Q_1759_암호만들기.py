L, C = map(int, input().split(" "))
alps = list(input().split(" "))
password = []

def sol(length, index, vowel_cnt):
    # base case
    if length == L:
        if vowel_cnt >= 1 and L - vowel_cnt >= 2:
            print("".join(password))
        return

    # recursive case
    if index < C:
        # password에 index 사용하는 경우
        # password[length] = alps[index]
        password.append(alps[index])
        v = int(is_vowel(alps[index]))
        sol(length + 1, index + 1, vowel_cnt + v)
        password.pop()

        # password에 index 사용하지 않는 경우
        sol(length, index + 1, vowel_cnt)

def is_vowel(alp):
    return alp == 'a' or alp == 'e' or alp == 'i' or alp == 'o' or alp == 'u'

alps.sort()
sol(0, 0, 0)
