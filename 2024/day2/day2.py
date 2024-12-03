
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

def 