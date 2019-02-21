from transactions import apply_transactions


balance = {
    'user1': 100,
    'user2': 500,
}

transactions = [
    {
        'user1': 50,
        'user2': 10
    },
    {
        'user1': 30,
        'user2': -100
    },
    {
        'user1': 100,
    },
    {
        'user2': -50
    }
]


apply_transactions(balance, transactions)