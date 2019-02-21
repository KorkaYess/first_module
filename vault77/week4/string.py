address = 'Tolebi 109A, 050040, Almaty, Kazakhstan'
post_code = '050048'
dirty_string = '  Something '


address.upper()   # создает новую строку, а оригинальная сохраняется
address.lower()

address.startswith('Almaty')  # returns False
post_code.startswith('0')     # returns True
dirty_string.startswith(' ')
dirty_string.startswith('  ')
dirty_string.startswith('   ')

address.endswith('n')
address.endswith('Kazakhstan')


address.find('Almaty')          # возвращает индекс

address.replace('Almaty', 'Astana')
address.replace(',', ';')

splt = address.split() # deleter, создает список с разделение на пробелы
' '.join(splt)

dirty_string.strip()

'40'.zfill(6) # ставит нули до необходимой длины строки (6)

history = [
    {
        'name': 'Alice',
        'age': 20
    },
    {
        'name': 'Bob',
        'age': 30
    },
    {
        'name': 'Eric',
        'age': 40
    },
]

name = history[0]['name']
age = history[0]['age']
'My name is {0}. My age is {1}'.format(name, age)


def find_six_digits(address):
    for i in range(len(address) - 6):
        substring = address[i:i + 6]
        if substring.isdigit():
            return substring

print(find_six_digits(address))
