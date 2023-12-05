data = []
with open('data.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', "")
        data.append(line)

non_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '.']
numbers_to_sum = []
# if its a digit
for index, row in enumerate(data):
    
    for i, j in enumerate(row):

        if j.isdigit():
            if data[index-1].isdigit() or  data[index-1] == '.':
                pass
            else:
                print("not done") 
