def d(series):
    return [b - a for a, b in zip(series, series[1:])]


def estimate(hist, row=0):
    if row == len(hist) - 1:
        return 0
    return hist[row][-1] + estimate(hist, row + 1)


with open("input") as f:
    data = [[int(n) for n in line.split()] for line in f.readlines()]

    sum = 0
    for series in data:
        hist = [series]
        while any(h != 0 for h in hist[-1]):
            hist.append(d(hist[-1]))
        sum += estimate(hist)

    print(sum)
