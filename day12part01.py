lines = []
with open('input/12.txt') as myFile:
    for line in myFile:
        lines.append(line)
        
def get_num_of_solutions(record, criteria):
    if len(record) == 0:
        if len(criteria) == 0:
            return 1
        return 0

    if len(criteria) == 0:
        if "#" not in record:
            return 1
        return 0

    result = 0

    if record[0] in ".?":
        result += get_num_of_solutions(record[1:], criteria)

    if record[0] in "#?":
        if len(record) >= criteria[0] and "." not in record[:criteria[0]] and (len(record) == criteria[0] or record[criteria[0]] != "#"):
            result += get_num_of_solutions(record[criteria[0] + 1:], criteria[1:])
        
    return result

sum_of_solutions = 0
for line in lines:
    record = line.split()[0]
    criteria = line.split()[1].split(',')
    criteria = [eval(i) for i in criteria]

    sum_of_solutions += get_num_of_solutions(record, criteria)
print(sum_of_solutions)
