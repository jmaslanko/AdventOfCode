import re

data = []

with open('data/day2.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', "")
        data.append(line)

bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

data_dict = {}
for game in data:
    values = game.split(':')
    game_id = int("".join([str(i) for i in values[0] if i.isdigit()]))
    red_cnts = [i for i in re.findall(r'(\d+) red', values[1])]
    
    
    data_dict[game_id] = red_cnts

