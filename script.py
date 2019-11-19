# -*- coding: cp866 -*-
import sys
from Main import *


number_of_records = int(sys.argv[1])
number_of_mistakes = float(sys.argv[2])
region = sys.argv[3]

if number_of_mistakes == 0:
    show_records_without_error(number_of_records, region)
elif number_of_mistakes < 1:
    show_records_with_mistakes_in_some(number_of_records, number_of_mistakes, region)
else:
    show_records_with_mistakes_in_each(number_of_records, number_of_mistakes, region)
