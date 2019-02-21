mounth = input('What mounth? ')
mounth = int(mounth)

if mounth > 0 and mounth < 4:
    print('It is winter')
if mounth > 3 and mounth < 7:
    print('It is spring')
if mounth > 6 and mounth < 10:
    print('It is summer')
if mounth > 9 and mounth < 13:
    print('It is outumn')