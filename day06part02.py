lines = []
with open('input/06.txt') as myFile:
    for line in myFile:
        lines.append(line)
times = lines[0]
distance = lines[1]

time  = times.split()
distance = distances.split()

time = int("".join(time[1:]))
distance = int("".join(distance[1:]))

num_of_ways = 0
for sec in range(0, time+1):
    if distance < sec*(time-sec):
        num_of_ways += 1

print(num_of_ways)
