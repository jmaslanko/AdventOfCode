# Part 1

left_list = []
right_list = []
with open("/Users/Jeremy/Documents/GitHub/AdventOfCode/2024/day1/data.csv", "r") as f:
    for line in f:
        output = line.split()
        left_list.append(int(output[0]))
        right_list.append(int(output[1]))

left_list.sort()
right_list.sort()

total_distance = 0
for i in range(0, len(left_list)):

    diff = abs(left_list[i] - right_list[i])
    total_distance += diff

# Part 2

total_score = 0
for i in left_list:
    right_list_cnt = right_list.count(i)
    similarity_score = right_list_cnt*i
    total_score += similarity_score