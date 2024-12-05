# Was pretty stuck from the get go, knew that I would need to look at each row and column
# and then look at indices of the surrounding letters for the match. Could visualize a brute
# force method, overthought it and decided to stop and watch some videos on how others approached it


def get_data(path: str) -> list:
    with open(path, "r") as f:
        data = []
        for line in f.readlines():
            data.append(line)
    return data


if __name__ == "__main__":
    data = get_data("/Users/Jeremy/Documents/GitHub/AdventOfCode/2024/day4/data.txt")

    height = len(data)
    width = len(data[0])

    count = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == "X" and data[row][col+1] == "M" and data[row][col+2] == "A" and data[row][col+3] == "S":
                count +=1

