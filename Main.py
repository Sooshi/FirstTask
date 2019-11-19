# -*- coding: cp866 -*-
from Recorder import *
from Errors import *


def create_record_with_error(number_of_errors, region):
    generated_record = create_record(region)
    return add_error_in_record(generated_record, number_of_errors)


def show_records_with_mistakes_in_some(number_of_records, error_chance, region):
    error_count = 1
    record_count_with_error = int(number_of_records) * error_chance
    for i in range(0, number_of_records):
        if i > record_count_with_error:
            record = create_record(region)
            print(record)
        else:
            record = create_record_with_error(number_of_records, region)
            print(record)


def show_records_with_mistakes_in_each(number_of_records, number_of_mistakes, region):
    error_count = int(number_of_mistakes)
    for i in range(0, number_of_records):
        record = create_record_with_error(error_count, region)
        print(record)


def show_records_without_error(number_of_records, region):
    for i in range(0, number_of_records):
        record = create_record(region)
        print(record)
