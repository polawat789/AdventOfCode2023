sum_num = 0
with open('input/01.txt') as myFile:
    for line in myFile:
        first = ""
        last = ""
        for char in line:
            if char.isdigit():
                if first == "":
                    first = char
                last = char
        sum_num += int(first+last)
print(sum_num)
