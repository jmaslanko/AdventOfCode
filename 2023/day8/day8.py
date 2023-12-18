data = []
with open('data.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', "")
        if line == '':
            pass
        else:
            data.append(line)

pattern = data[0]
mappings = {}

for i in data[1:]:
    key = i.split("=")[0].strip()
    values = i.split("=")[1].replace("(","").replace(")","").replace(" ", "").split(",")
    mappings[key] = values

    
    
start = 'AAA'
end = 'ZZZ'
next_pos = ''
pattern_loc = 0

for move in pattern:
    
    if move == 'L':
        index = 0
    else:
        index = 1

    if pattern_loc == 0:
        next_pos = mappings[start][index]
    else:
        next_pos = mappings[next_pos][index]
    
    if next_pos == 'ZZZ':
        break

