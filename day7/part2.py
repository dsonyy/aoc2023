def key(hand):
    hand = [ch for ch in hand]
    for i in range(len(hand)):
        if hand[i] == "T":
            hand[i] = 10
        elif hand[i] == "J":
            hand[i] = 1
        elif hand[i] == "Q":
            hand[i] = 12
        elif hand[i] == "K":
            hand[i] = 13
        elif hand[i] == "A":
            hand[i] = 14
        else:
            hand[i] = int(hand[i])

    cnt = [0 for _ in range(15)]
    for c in hand:
        cnt[c] += 1

    code = []
    if cnt[1] != 0:
        if 5 in cnt:
            code.append(10)
        elif 4 in cnt:
            code.append(10)
        elif 3 in cnt and 2 in cnt:
            code.append(10)
        elif 3 in cnt:
            code.append(9)
        elif 2 in cnt and cnt.count(2) == 2 and cnt[1] == 1:
            code.append(8)
        elif 2 in cnt and cnt.count(2) == 2 and cnt[1] == 2:
            code.append(9)
        elif 2 in cnt:
            code.append(7)
        else:
            code.append(5)
    else:
        if 5 in cnt:
            code.append(10)
        elif 4 in cnt:
            code.append(9)
        elif 3 in cnt and 2 in cnt:
            code.append(8)
        elif 3 in cnt:
            code.append(7)
        elif 2 in cnt and sum(v for v in cnt if v != 1) == 4:
            code.append(6)
        elif 2 in cnt:
            code.append(5)
        else:
            code.append(4)

    code += hand
    return code


with open("input") as f:
    data = [(v.split()[0], int(v.split()[1])) for v in f.readlines()]
    data.sort(key=lambda hand: key(hand[0]))
    r = sum((no + 1) * row[1] for no, row in enumerate(data))
    print(r)
