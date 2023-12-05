import pandas as pd

number_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}


def number_replace(code: str):
    for number in number_dict:
        code = code.replace(number, str(number_dict[number]))

    return code

def get_numbers(code: str):
    
    all_numbers = [value for value in code if value.isnumeric()]
    number = str(all_numbers[0]) + str(all_numbers[-1])

    return int(number)

if __name__ == "__main__":
    data = pd.read_csv('data/day1.csv', header=None)
    data['no_text_nums'] = data[0].apply(number_replace)
    data['num_col'] = data['no_text_nums'].apply(get_numbers)
    sum = data['num_col'].sum()