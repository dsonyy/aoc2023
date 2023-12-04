import re

with open("input") as f:
    sum = 0
    for line in f:
        winning, yours = [set(int(val) for val in group.split())
                          for group in re.sub(r"Card +\d+:", "", line).split("|")]

        inter = yours.intersection(winning)
        score = 2**(len(inter)-1) if len(inter) else 0

        sum += score
    print(sum)
