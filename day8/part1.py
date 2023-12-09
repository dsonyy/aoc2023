with open("input") as f:
    data = f.read().splitlines()

    dirs = data[0].strip().split()[0]
    maps = {}

    for i in range(2, len(data)):
        row = data[i]
        a = row.split()[0]
        l = row.split()[2][1:-1]
        r = row.split()[3][0:-1]
        maps[a] = (l, r)

    i = 0
    j = 0
    pos = "AAA"
    while pos != "ZZZ":
        if dirs[j] == "L":
            pos = maps[pos][0]
        elif dirs[j] == "R":
            pos = maps[pos][1]
        j = (j + 1) % len(dirs)
        i += 1

    print(i)
