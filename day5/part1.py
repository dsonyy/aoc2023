import re

seeds = []
maps = [[] for _ in range(7)]

with open("input") as f:
    mapi = -1
    for line in f:
        if line.strip() == "":
            continue

        if "seeds" in line:
            seeds = [int(s) for s in line.split()[1:]]
            continue

        if re.match(".* map\:", line):
            mapi += 1
            continue

        dst, src, n = [int(v) for v in line.split()]
        maps[mapi].append((dst, src, n))

print(maps)

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
print(poses)
print(min(poses))
