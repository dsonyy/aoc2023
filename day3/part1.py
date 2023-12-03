
def issymbol(c):
    return c != "." and not c.isdigit()


with open("input") as f:
    arr = ["." + x.strip() + "." for x in f.readlines()]
    dummy_row = ["." * len(arr[0])]
    arr =  dummy_row + arr + dummy_row
    
    sum = 0
    for y in range(1, len(arr) - 1):
        start = None
        end = None
        
        # Selecting numbers
        for x in range(1, len(arr[0])):
            if arr[y][x].isdigit() and start is None:
                start = x
            elif not arr[y][x].isdigit() and start is not None:
                end = x

                # Checking neighbors
                if issymbol(arr[y][start - 1]) or issymbol(arr[y][end]):
                    sum += int(arr[y][start:end])
                else:
                    for x0 in range(start - 1, end + 1):
                        if issymbol(arr[y - 1][x0]) or issymbol(arr[y + 1][x0]):
                            sum += int(arr[y][start:end])
                            break
                
                start = None
                end = None

    print(sum)