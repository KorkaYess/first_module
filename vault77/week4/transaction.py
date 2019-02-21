def  apply_transactions(balance, transactions):
    for transaction in transactions:
        lst = list(transaction.keys())
        for i in range(len(lst)):
            user = lst[i]
            change = transaction.get(user, 0)
            user_balance = balance[user]
            balance[user] = user_balance + change
            print(lst, user, change, user_balance)

    print(balance)

if __name__ == '__main__':
    balance = {'user1': 100, 'user2': 500}
    transactions = [
        {'user1': 50, 'user2': 10},
        {'user1': 30, 'user2': -10},
        {'user1': 100}, {'user2': -50}]
    apply_transactions(balance, transactions)
    assert balance == {'user1': 280, 'user2': 450}