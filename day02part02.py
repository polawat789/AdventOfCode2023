lines = []
with open('input/02.txt') as myFile:
    for line in myFile:
        lines.append(line)
sumOfPowers = 0
for line in lines:
    red = 0
    redMax = 0

    blue = 0
    blueMax = 0

    green = 0
    greenMax = 0

    line += ";"
    
    lineSplit = line.split(":")
    game = lineSplit[1].split(" ")
    for x in range(0, len(game)):
        if "red" in game[x]:
            red += int(game[x-1])
        elif "blue" in game[x]:
            blue += int(game[x-1])
        elif "green" in game[x]:
            green += int(game[x-1])
    
        if ";" in game[x]:
            redMax = max(redMax, red)
            blueMax = max(blueMax, blue)
            greenMax = max(greenMax, green)

            red = 0
            blue = 0
            green = 0
    sumOfPowers += redMax*blueMax*greenMax
print(sumOfPowers)
