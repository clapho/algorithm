class Egg(object):
    def __init__(self, durability, weight):
        self.durability = durability
        self.weight = weight

    def fight(self, other_egg):
        self.durability -= other_egg.weight
        other_egg.durability -= self.weight

    def restore(self, other_egg):
        self.durability += other_egg.weight
        other_egg.durability += self.weight

N = int(input())
eggs = []
ans = 0

for i in range(N):
    durability, weight = map(int, input().split(" "))
    egg = Egg(durability, weight)
    eggs.append(egg)

def break_egg(pick):
    global ans

    # base case
    if pick == N:
        cnt = 0
        for i in range(N):
            if eggs[i].durability < 0:
                cnt += 1
                ans = max(ans, cnt)
        return

    # recursive case

    if eggs[pick].durability > 0:
        target_exists = False
        for target in range(N):
            if target == pick: continue
            if eggs[target].durability > 0:
                target_exists = True
                eggs[pick].fight(eggs[target])
                break_egg(pick + 1)
                eggs[pick].restore(eggs[target])

        if not target_exists:
            break_egg(pick + 1)
    else:
        break_egg(pick + 1)

break_egg(0)
print(ans)
