
stones = [2, 7, 4, 1, 8, 1]


def lastStoneWeight(stones):
    while len(stones) >= 2:
        stones.sort(reverse=True, key=int)
        if stones[0] == stones[1]:
            stones = stones[2:]
        else:
            y = [abs(stones[0] - stones[1])]
            stones = y + stones[2:]

    if len(stones) == 1:
        return stones[0]
    else:
        return 0


def lastStoneWeight2(stones):
    stones.sort()
    while len(stones) > 1:
        if stones[-1] == stones[-2]:
            stones = stones[:-2]
        else:
            stones = stones[:-2] + [abs(stones[-2] - stones[-1])]
        stones.sort()

    if stones:
        return stones[0]
    else:
        return 0


x = lastStoneWeight(stones)
print(x)
