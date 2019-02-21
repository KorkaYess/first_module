balance = {
    'user1': 100, 
    'user2': 500,
    'user3': 150
}

transactions = [
    {'user1': -10},
    {'user2': -20},
    {'user3': -40},
    {'user1': 50},
    {'user2': -20},
    {'user3': 60},
    {'user2': -100}
]
def apply_transactions(balance, transactions):
    for transaction in transactions:
        user = list(transaction.keys())[0]
        change = transaction[user]
        user_balance = balance[user]
        balance[user] = user_balance + change
    print(balance)


apply_transactions(balance, transactions)