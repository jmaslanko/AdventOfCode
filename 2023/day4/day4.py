data = []
with open('data.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', "")
        data.append(line)

total_score = 0

for card in data:
    all_data_list = [i for i in card.split(':')]
    
    num_list = [i.strip() for i in all_data_list[1].split('|')]
    winning_nums = [int(i) for i in num_list[0].split()]
    my_nums = [int(i) for i in num_list[1].split()]
    
    cards_have = 0
    for num in my_nums:
        if num in winning_nums:
            cards_have += 1
    
    if cards_have == 0:
        total = 0
    elif cards_have == 1:
        total = 1
    else:
        total = 1 * (2**(cards_have-1))

    total_score += total
    
    print(all_data_list, len(winning_nums), len(my_nums), cards_have)
print(total_score)
