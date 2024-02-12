platform = []
with open('input/14.txt') as myFile:
    for line in myFile:
        platform.append(line.rstrip())
        
def solve(platform):
    total = 0
    for col in list(zip(*platform)):
        last_value = len(col)
        for index in range(0, len(col)):
            if col[index] == "O":
                for i in reversed(range(0, index)):
                    if col[i] == "O":
                        last_value -= 1
                        break
                    elif col[i] == "#":
                        last_value = len(col) - 1 - i
                        break
                total += last_value
    return total
                
print(solve(platform))
