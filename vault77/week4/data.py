from calculate_balance import calculate_balance


balance = {
    'Alice': 100,
    'Bob': 100,
    'Charlie': 5000,
    'Eric': 50,
    'Fiona': 300
}

plans = {
    'cheap': 1,
    'average': 2,
    'expensive': 10
}

users = {
    'Alice': 'cheap',
    'Bob': 'average',
    'Charlie': 'expensive',
    'Fiona': 'cheap'
}

history = [
    {
        'user': 'Charlie',
        'duration': 50
    },
    {
        'user': 'Alice',
        'duration': 10
    },
    {
        'user': 'Alice',
        'duration': 20
    },
    {
        'user': 'Bob',
        'duration': 2
    },
    {
        'user': 'Eric',
        'duration': 15
    },
]


calculate_balance(balance, plans, users, history)