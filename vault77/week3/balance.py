balance = {
    'user1': 100, 
    'user2': 500
}

transactions = [
    {'user1': -10},
    {'user2': -20},
    {'user1': 50},
    {'user2': -20},
    {'user2': -200}
]

def apply_transactions(balance, transactions):
    
    users = []
    
    for key, value in balance.items():
        users.append(key)

    for i in transactions:
        for key, value in i.items():
            if key == users[0]:
                balance[users[0]] = balance[users[0]] + value
            else:
                balance[users[1]] = balance[users[1]] + value
    return balance

print(apply_transactions(balance, transactions))