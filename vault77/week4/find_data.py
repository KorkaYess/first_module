import datetime
import re


def print_dates():

    with open('find_data.txt') as dates:
        dates_str = dates.read()
        pattern = '\d{4}.\d{2}.\d{2}'
        result = re.findall(pattern, dates_str)

        return result
 

print(print_dates())

f = open('find_data.txt')
assert print_dates() == ['2018.10.01', '1984.05.06', '1990.10.11', '2012.12.12']
