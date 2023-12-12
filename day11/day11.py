with open("input") as f:
    data = [line.strip() for line in f.readlines()]
    rows = [i for i in range(len(data)) if all(ch == '.' for ch in data[i])]
    cols = [i for i in range(len(data[0])) if all(
        line[i] == '.' for line in data)]

    def dist(x0, y0, x1, y1, n):
        d = abs(x0 - x1) + abs(y0 - y1)
        for row in rows:
            if y0 < row < y1 or y1 < row < y0:
                d += n - 1
        for col in cols:
            if x0 < col < x1 or x1 < col < x0:
                d += n - 1
        return d

    gxs = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '#':
                gxs.append((x, y))

    sum1 = 0
    sum2 = 0
    for i in range(len(gxs)):
        for j in range(i+1, len(gxs)):
            a = gxs[i]
            b = gxs[j]
            sum1 += dist(a[0], a[1], b[0], b[1], 2)
            sum2 += dist(a[0], a[1], b[0], b[1], 1000000)

    print(sum1, sum2)
