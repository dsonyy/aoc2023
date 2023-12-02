sum = 0

with open("input") as f:
    for line in f:
        possible = True

        game, line = line.split(": ")
        game = game.split("Game ")[1]

        sets = line.split(";")
        for set in sets:
            red = 12
            green = 13
            blue = 14

            x = set.split(",")
            for pair in x:
                num, col = pair.strip().split(" ")
                num = int(num)
                
                if col == "red":
                    red -= num
                elif col == "green":
                    green -= num
                elif col == "blue":
                    blue -= num
                
                if red < 0 or green < 0 or blue < 0:
                    possible = False
                    break
            
            if not possible:
                break
        
        if possible:
            sum += int(game)

print(sum)
