from sys import stdin
engine_schematic = []
with open('input/03.txt') as myFile:
    for line in myFile:
        engine_schematic.append(line.rstrip())


symbols = "[]\{\}|\\!@#$%^&*()_-+=;:'\"<>,/?`~"

sum_of_part_numbers = 0
for row in range(0, len(engine_schematic)):
    col = 0
    while col < len(engine_schematic[0]):
        if engine_schematic[row][col].isdigit():
            start = col
            end = col

            while end < len(engine_schematic[0]) and engine_schematic[row][end].isdigit():
                end += 1

            for x in range(start, end):
                if row != 0:
                    if x != 0 and engine_schematic[row-1][x-1] in symbols:
                        sum_of_part_numbers += int(engine_schematic[row][start:end])
                        break
                    if x+1 < len(engine_schematic[0]) and engine_schematic[row-1][x+1] in symbols:
                        sum_of_part_numbers += int(engine_schematic[row][start:end])
                        break
                    if engine_schematic[row-1][x] in symbols:
                        sum_of_part_numbers += int(engine_schematic[row][start:end])
                        break

                if x != 0 and engine_schematic[row][x-1] in symbols:
                    sum_of_part_numbers += int(engine_schematic[row][start:end])
                    break

                if x+1 < len(engine_schematic[0]) and engine_schematic[row][x+1] in symbols:
                    sum_of_part_numbers += int(engine_schematic[row][start:end])
                    break

                if row < len(engine_schematic) - 1 :
                    if x != 0 and engine_schematic[row+1][x-1] in symbols:
                        sum_of_part_numbers += int(engine_schematic[row][start:end])
                        break
                    if x+1 < len(engine_schematic[0]) and engine_schematic[row+1][x+1] in symbols:
                        sum_of_part_numbers += int(engine_schematic[row][start:end])
                        break
                    if engine_schematic[row+1][x] in symbols:
                        sum_of_part_numbers += int(engine_schematic[row][start:end])
                        break        



            col = end
        col += 1

print(sum_of_part_numbers)
