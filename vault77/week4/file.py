with open('customers.txt') as f:

    customers = []
    for customer in f.readlines():
        name, age, product = customer.split(',')
        customers.append({
            'name': name,
            'age': int(age.strip()),
            'product': product.strip()
        })

print(customers)
david = {'name': 'David', 'age': 25, 'product': 'orange'}
david_str = '\n{}, {}, {}'.format(david['name'], david['age'], david['product'])

with open('customers.txt', 'a') as f:# 'a' - append т.е. добавляем в файл нового пользователя
    f.write(david_str)
