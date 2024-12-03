
def get_data(path: str) -> list:
    with open(path, "r") as f:
        data = []
        for line in f.readlines():
            row = line.split()
            row = [int(i) for i in row]
            data.append(row)
    return data

def is_safe(report: list) -> bool:

    counter = 0
    difference = []
    for i in range(1, len(report)):
        difference.append(abs(report[i]-report[i-1]))
        if report[i] > (report[i-1]):
            counter += 1
        elif report[i] < (report[i-1]):
            counter -= 1
        else:
            counter += 0

    if (abs(counter) == len(report)-1) and max(difference)<=3:
        return True
    else:
        return False

def main(data: list):
    safe_floors_one = 0
    safe_floor_two = 0
    for row in data:
        if is_safe(row):
            safe_floors_one += 1
        else:
            for i in range(len(row)):
                new = row[:i] + row[i+1:]
                if is_safe(new):
                    safe_floor_two += 1
                    break

    print(f"Part one: {safe_floors_one}")
    print(f"Part two: {safe_floor_two+safe_floors_one}")



if __name__ == "__main__":
    data = get_data("/Users/Jeremy/Documents/GitHub/AdventOfCode/2024/day2/data.txt")
    main(data)