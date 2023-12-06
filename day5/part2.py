import re

ranges = []
maps = [[] for _ in range(7)]
inters = set([])

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
        inters.add(src)
        inters.add(src+n+1)
        inters.add(dst)
        inters.add(dst+n+1)

ranges2 = []
for range_ in ranges:
    start, n = range_
    inters2 = []
    for inter in inters:
        if start <= inter and inter < start+n:
            inters2.append(inter)

    if len(inters2) == 0:
        ranges2.append((start, n))
    else:
        for i in range(len(inters2)):
            if i == 0:
                ranges2.append((start, inters2[i] - start))
            else:
                ranges2.append((inters2[i-1], inters2[i] - inters2[i-1]))
        ranges2.append((inters2[-1], start+n - inters2[-1]))


print(ranges)
print(inters)
# print(ranges2)

seeds = [r[0] for r in ranges2]
# print(seeds)

poses = []
for seed in seeds:
    pos = seed
    for map in maps:
        for record in map:
            dst, src, n = record
            if src <= pos and pos < src + n:
                pos += dst - src
                break
    poses.append(pos)
print(min(poses))
# 6472060
