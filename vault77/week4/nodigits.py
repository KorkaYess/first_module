import re
string = 'Alice is 21 years old'


def nodigits(string):
    pattern = '\d'
    nodigit_list = re.split(pattern, string)
    result = ' '.join(nodigit_list)
    print(result.replace('    ',' '))
    return result


assert nodigits(string) == 'Alice is    years old'
assert nodigits('3 times a day he drinks 2 liters of water') == '  times a day he drinks   liters of water'
assert nodigits('Bob is 30 years old and have 3cats') == 'Bob is    years old and have  cats'