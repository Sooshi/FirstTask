# -*- coding: cp866 -*-
from database import info
import random


def create_record(region):
    data = info[region]
    first_name = random.choice(data[0])
    last_name = random.choice(data[1])
    phone_num = phone_num_generator(data[2], region)
    address = generate_address(data[3], region)
    fio = first_name + ' ' + last_name
    if region != 'en_US':
        surname = random.choice(data[4])
        fio += ' ' + surname
    return [fio, phone_num, address]


def phone_num_generator(codes, region):
    phone_code = random.choice(codes)
    number = str(random.randint(1000000, 9999999))
    if region == 'by_BY':
        return '+375' + phone_code + number
    elif region == 'ru_RU':
        return '8' + phone_code + number
    else:
        return phone_code + number


def generate_address(streets, language):
    street = random.choice(streets)
    house_num = str(random.randint(1, 100))
    if language != 'en_US':
        house_num += random.choice(['', 'A', 'Б'])
        return street + ' ' + house_num
    else:
        return house_num + ' ' + street
