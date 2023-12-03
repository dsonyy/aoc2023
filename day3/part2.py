def findnum(arr, y, x):
    if not arr[y][x].isdigit():
        return None

    start = x
    end = x + 1

    # Finding start
    while arr[y][start - 1].isdigit():
        start -= 1
    
    # Finding end
    while arr[y][end].isdigit():
        end += 1
    
    result = int(arr[y][start:end])

    # Erase number
    arr[y] = arr[y][:start] + "." * (end - start) + arr[y][end:]

    return result


with open("input") as f:
    arr = ["." + x.strip() + "." for x in f.readlines()]
    dummy_row = ["." * len(arr[0])]
    arr =  dummy_row + arr + dummy_row
    
    sum = 0
    for y in range(1, len(arr) - 1):
        for x in range(1, len(arr[0])):
            
            # Finding gears
            if arr[y][x] == "*":
                value = 1

                # Checking neighbors for numbers
                cnt = 2
                if arr[y][x - 1].isdigit() or arr[y][x + 1].isdigit():
                    if v := findnum(arr, y, x - 1): 
                        cnt -= 1
                        value *= v
                        print(v)
                    if v := findnum(arr, y, x + 1):
                        cnt -= 1 
                        value *= v
                        print(v)
            
                for x0 in range(x - 1, x + 2):
                    if arr[y - 1][x0].isdigit() or arr[y + 1][x0].isdigit():
                        if (v := findnum(arr, y - 1, x0)) and cnt: 
                            cnt -= 1
                            value *= v
                            print(v)
                        if (v := findnum(arr, y + 1, x0)) and cnt:
                            cnt -= 1
                            value *= v
                            print(v)

                        if cnt == 0: break
                    if cnt == 0: break
                
                print("*" if cnt == 0 else "x")
                
                # Add only if two numbers were found
                if cnt == 0:
                    sum += value

    print(sum)