sum_num = 0
with open('input/01.txt') as myFile:
    for line in myFile:
        line = line.replace("one", "on1e")
        line = line.replace("two", "tw2o")
        line = line.replace("three", "thr3ee")
        line = line.replace("four", "fo4ur")
        line = line.replace("five", "fiv5e")
        line = line.replace("six", "si6x")
        line = line.replace("seven", "se7ven")
        line = line.replace("eight", "eig8ht")
        line = line.replace("nine", "ni9ne")
        first = ""
        last = ""
        for char in line:
            if char.isdigit():
                if first == "":
                    first = char
                last = char
        sum_num += int(first+last)
print(sum_num)
