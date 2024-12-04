import re


def get_data(path: str) -> list:
    with open(path, "r") as f:
        data = ''
        for line in f.readlines():
            data += line
    return data


def part_one(data: str):
    pattern = re.compile(r"mul\(\d{1,3}\,\d{1,3}\)")
    matches = pattern.findall(data)

    digit_pattern = re.compile(r"\d{1,3}")

    sum = 0
    for match in matches:
        numbers = digit_pattern.findall(match)

        product = int(numbers[0])*int(numbers[1])
        sum += product
    
    print(sum)


def part_two(data: str):
    pattern = re.compile(r"do\(\)|mul\(\d{1,3}\,\d{1,3}\)|don\'t\(\)")
    matches = pattern.findall(data)
    
    do = "do()"
    dont = "don't()"

    digit_pattern = re.compile(r"\d{1,3}")

    sum = 0
    status = True
    for match in matches:
        if match == do:
            status = True
        elif match == dont:
            status = False
        else:
            if status == True:
                numbers = digit_pattern.findall(match)

                product = int(numbers[0])*int(numbers[1])
                sum += product
    
    print(sum)


if __name__ == "__main__":
    data = get_data("/Users/Jeremy/Documents/GitHub/AdventOfCode/2024/day3/data.txt")
    part_one(data)
    part_two(data)