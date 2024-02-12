lines = []
with open('input/06.txt') as myFile:
    for line in myFile:
        lines.append(line)
times = lines[0]
distance = lines[1]

time_split = times.split()
distance = distance.split()

index = 1
margin_error = 1
for time in time_split[1:]:
    num_of_ways = 0
    for sec in range(0, int(time)+1):
        if int(distance[index]) < sec*(int(time) - sec):
            num_of_ways += 1
    margin_error *= num_of_ways
    index += 1
print(margin_error)
