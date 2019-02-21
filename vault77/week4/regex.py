import re

address = 'Tolebi 109A, 050040, 050040, Almaty, Kazakhstan, 045040, 050041'
# match = re.search('\d{6}', address) # только цифры из 6 знаков
# print(match.group(0)) # находит только первое совпадение
# print(re.findall('\d{6}', address)) # вернет список

pattern = '\d{3}[A-Z]'
match = re.search(pattern, address)
print(re.findall(pattern, address))