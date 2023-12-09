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

    results = []
    for a, (l, r) in maps.items():
        if a[-1] != "A":
            continue

        i = 0
        j = 0
        pos = a
        while pos[-1] != "Z":
            if dirs[j] == "L":
                pos = maps[pos][0]
            elif dirs[j] == "R":
                pos = maps[pos][1]
            j = (j + 1) % len(dirs)
            i += 1
        results.append(i)

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def lcm(a, b):
        return abs(a * b) / gcd(a, b)

    def lcm2(nums):
        if len(nums) == 2:
            return int(lcm(nums[0], nums[1]))

        elif len(nums) == 1:
            return int(nums[0])

        return lcm2([lcm(nums[0], nums[1])] + nums[2:])

    print(lcm2(results))
