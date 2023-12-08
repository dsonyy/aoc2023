import re

ranges = []
maps = [[] for _ in range(7)]

with open("input") as f:
    mapi = -1
    for line in f:
        if line.strip() == "":
            continue

        if "seeds" in line:
            seeds = [int(s) for s in line.split()[1:]]
            ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
            continue

        if re.match(".* map\:", line):
            mapi += 1
            continue

        dst, src, n = [int(v) for v in line.split()]
        maps[mapi].append((dst, src, n))


def f():
    for dstt in range(46, 10000000000):
        pos = dstt
        for map in maps[::-1]:
            for record in map:
                dst, src, n = record
                if dst <= pos and pos < dst + n:
                    pos -= dst - src
                    break

        for range_ in ranges:
            if range_[0] <= pos and pos < range_[0] + range_[1]:
                return dstt


print(f())
