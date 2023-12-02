def check(str, reversed=False):
    if reversed:
        str = str[::-1]

    if str[0] in "0123456789":
        return str[0]
    
    words = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for k, v in words.items():
        if reversed:
            k = k[::-1]

        if str[:len(k)] == k:
            return v
    
    return ""


with open("input") as f:
    sum = 0
    for line in f:
        num = ""

        for i in range(len(line)):
            ch = check(line[i:])
            if ch != "":
                num += ch
                break

        for i in range(len(line), 0, -1):
            ch = check(line[:i], reversed=True)
            if ch != "":
                num += ch
                break

        sum += int(num)
    print(sum)  