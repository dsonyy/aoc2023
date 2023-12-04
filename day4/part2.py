import re

with open("input") as f:
    sum = 0
    vals = {}
    for no, line in enumerate(f):
        winning, yours = [set(int(val) for val in group.split())
                          for group in re.sub(r"Card +\d+:", "", line).split("|")]
        score = len(yours.intersection(winning))
        vals[no] = score

    def process(vals, no):
        global sum
        sum += 1

        if vals[no] == 0:
            return

        for no2 in range(no + 1, no + 1 + vals[no]):
            process(vals, no2)

    for no in vals.keys():
        process(vals, no)

    print(sum)
