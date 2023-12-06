
with open("input") as f:
    times = [int(v) for v in f.readline().split()[1:]]
    dists = [int(v) for v in f.readline().split()[1:]]

result = 1
for i_race in range(len(times)):
    time = times[i_race]
    dist = dists[i_race]

    cnt = 0
    for t in range(0, time + 1):
        score = (time - t) * t
        if score > dist:
            cnt += 1

    result *= cnt
print(result)
