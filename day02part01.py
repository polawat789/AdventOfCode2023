lines = []
with open('input/02.txt') as myFile:
    for line in myFile:
        lines.append(line)
sumOfIds = 0
for line in lines:
    red = 0
    blue = 0
    green = 0
    isReal = True
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
            if red > 12 or blue > 14 or 13 < green:
                isReal = False
            red = 0
            blue = 0
            green = 0

    if isReal:
        sumOfIds += int(lineSplit[0].split(" ")[1])
print(sumOfIds)
