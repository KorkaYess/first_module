def  apply_transactions(balance, transactions):
    for transaction in transactions:
        users = list(transaction.keys())
        # for transaction in transactions
            # for user, values in transaction.items()
        for user in range(len(users)):
            user_ = users[user]
            change = transaction.get(user_, 0)
            user_balance = balance[user_]
            balance[user_] = user_balance + change

    print(balance)

if __name__ == '__main__':
    balance = {'user1': 100, 'user2': 500}
    transactions = [
        {'user1': 50, 'user2': 10},
        {'user1': 30, 'user2': -10},
        {'user1': 100}, {'user2': -50}]
    apply_transactions(balance, transactions)
    assert balance == {'user1': 280, 'user2': 450}

    balance = {'user1': 100, 'user2': 500, 'user3': 200}
    transactions = [
        {'user1': 50, 'user2': 10},
        {'user1': 30, 'user2': -10},
        {'user1': 100, 'user3': -50}, {'user2': -50}]
    apply_transactions(balance, transactions)
    assert balance == {'user1': 280, 'user2': 450, 'user3': 150}

    balance = {'user1': 50, 'user2': 1000}
    transactions = [
        {'user1': 50, 'user2': -350},
        {'user1': 30, 'user2': -150},
        {'user1': 100}, {'user2': -500, 'user1': 100}]
    apply_transactions(balance, transactions)
    assert balance == {'user1': 380, 'user2': 0}
