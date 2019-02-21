chislo = 49
vvod = input('Find a number: ')
vvod = int(vvod)
count = 1

while vvod != chislo:
    vvod = int(vvod)
    if vvod >= 0 and vvod <= 20:
        vvod = input('Ochen holodno, poprobyite ewe: ')
        vvod = int(vvod)
        count = count + 1
    if vvod >= 20 and vvod <= 39:
        vvod = input('Holodno, poprobyite ewe: ')
        vvod = int(vvod)
        count = count + 1
    if vvod >= 39 and vvod <= 44:
        vvod = input('Teplo, poprobyite ewe: ')
        vvod = int(vvod)
        count = count + 1
    if vvod >= 44 and vvod <= 47:
        vvod = input('Teplee, poprobyite ewe: ')
        vvod = int(vvod)
        count = count + 1
    if vvod >= 47 and vvod < 49:
        vvod = input('Goryacho, poprobyite ewe: ')
        vvod = int(vvod)
        count = count + 1
    if vvod <= 100 and vvod >= 80:
        vvod = input('Ochen holodno, poprobyite ewe: ')
        vvod = int(vvod)
        count = count + 1
    if vvod <= 80 and vvod >= 59:
        vvod = input('Holodno, poprobyite ewe: ')
        vvod = int(vvod)
        count = count + 1
    if vvod <= 59 and vvod >= 54:
        vvod = input('Teplo, poprobyite ewe: ')
        vvod = int(vvod)
        count = count + 1
    if vvod <= 54 and vvod >= 51:
        vvod = input('Teplee, poprobyite ewe: ')
        vvod = int(vvod)
        count = count + 1
    if vvod <= 51 and vvod > 49:
        vvod = input('Goryacho, poprobyite ewe: ')
        vvod = int(vvod)
        count = count + 1
    if vvod < 0:
        vvod = input('Moroz: ')
        vvod = int(vvod)
        count = count + 1
    if vvod > 100:
        vvod = input('Moroz: ')
        vvod = int(vvod)
        count = count + 1

print('You WIN on ' + str(count) + 'th try')