# customers = open('customers.txt', 'r')    # 'r' - read считывание файла(по умолчанию)

# print(customers.readline())
# print(customers.readline())

# print(customers.readlines())
# for customer in customers.readlines():
    # print(customer)

# customers.close()


f = open('customers.txt')

customers = []
for customer in f.readlines():
    name, age, product = customer.split(',')
    customers.append({
        'name': name,
        'age': int(age.strip()),
        'product': product.strip()
    })

f.close()

print(customers)
david = {'name': 'David', 'age': 25, 'product': 'orange'}
david_str = '\n{}, {}, {}'.format(david['name'], david['age'], david['product'])

f = open('customers.txt', 'a')  # 'a' - append т.е. добавляем в файл нового пользователя
f.write(david_str)
f.close