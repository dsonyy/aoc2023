
with open("input") as f:
    sum = 0
    for line in f:
        num = ""
        for ch in line:
            if ch in "0123456789":
                num += ch
                break
        for ch in line[::-1]:
            if ch in "0123456789":
                num += ch
                break
        sum += int(num)
    print(sum)  