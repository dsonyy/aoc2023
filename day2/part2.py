sum = 0

with open("input") as f:
    for line in f:
        possible = True

        game, line = line.split(": ")
        game = game.split("Game ")[1]


        red = 0
        green = 0
        blue = 0
        sets = line.split(";")
        for set in sets:
            

            x = set.split(",")
            for pair in x:
                num, col = pair.strip().split(" ")
                num = int(num)
                
                if col == "red":
                    red = max(red, num)
                elif col == "green":
                    green = max(green, num)
                elif col == "blue":
                    blue = max(blue, num)
                
        
        sum += (red * green * blue)

print(sum)