orders = ['apple', 'banana', 'orange', 'apple', 'apple', 'orange']

def build_dict(orders): #функция строит словарь, считает сколько заказывали каждый элемент
    counter = {}
    for item in orders:
        item_counter = counter.get(item)
        if item_counter is None:
            counter[item] = 1
        else:
            counter[item] = item_counter + 1
    return counter

def max_key(counter): #
    max_item = ''
    max_count = 0 
    for item, count in counter.items():
        if count > max_count:
            max_item = item
            max_count = count
    return max_item

counter = {item: orders.count(item) for item in set(orders)}
print(counter)
most_popular = max(counter, key = counter.get)
print(most_popular)