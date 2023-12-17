
input = {"Time":[56,97,78,75],
         "Distance": [546,1927,1131,1139]}

input_pt2 = {"Time":[56977875],
         "Distance": [546192711311139]}




total_nums_beat = []
for index, time in enumerate(input_pt2["Time"]):

    num_times_beat = 0
    for i in range(0, time+1):
        
        time_held = i
        time_remaining = time - i

        distance = time_held * time_remaining

        if distance > input_pt2["Distance"][index]:
            num_times_beat += 1
    total_nums_beat.append(num_times_beat)

time = 71530
test = 0
for i in range(0, time+1)[:15]:
        
    time_held = i
    time_remaining = time - i

    distance = time_held * time_remaining
    print(distance, 940200)
    if distance > 940200:
        test += 1
    