# -*- coding: cp866 -*-
import random
import string


def add_error_in_record(record, number_of_mistakes):
    count_elements = 2
    for i in range(0, int(number_of_mistakes)):
        data_number = random.randint(0, count_elements)
        data = record[data_number]
        replaced_char = random.randint(0, len(data))
        action = random.choice(actions)
        record[data_number] = action(data, replaced_char)
    return record


def replace_char(data, index):
    return data[:index] + random_char() + data[index+1:]


def delete_char(data, index):
    return data[:index] + '' + data[index+1:]


def add_char(data, index):
    return data[:index] + random_char() + data[index:]


actions = [add_char, delete_char, add_char]


def random_char(min_chars=1, max_chars=1, alphabet=string.ascii_lowercase):
    return ''.join(random.choice(alphabet))
