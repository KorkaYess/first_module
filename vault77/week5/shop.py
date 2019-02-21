class Item:

    def __init__(self, name, price, is_adult_only):
        self.name = name
        self.price = price
        self.is_adult_only = is_adult_only


class Cart:

    def __init__(self, customer):
        self.customer = customer

    # создает словарь из продуктов и их количества в корзине
    def add_to_cart(self, item, quantity):
        if item.is_adult_only:
            if self.customer.age >= 18:
                self.customer.cart[item] = quantity
            else:
                print ("Sorry, {}, you're underage and can't buy {}".format(self.customer.name, item.name))
        else:
            self.customer.cart[item] = quantity


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cart = {}

    def check(self):  # высчитывает чек
        eachproduct_price = {item: item.price * self.cart[item] for item in self.cart}
        return sum(eachproduct_price.values())

    def pay(self, payment):  # принимает оплату
        amount = self.check()
        if payment < amount:  # требует довнести оплату, если взноса не достаточно
            amount = amount - payment
            while amount > 0:
                residual_payment = input('Your amount is not enough, {} KZT left: '.format(amount))
                amount = amount - int(residual_payment)
        else:  # расчитывает сдачу и очищает словарь, если все оплачено
            charge = payment - amount
            print('{}, Your charge is {} KZT'.format(self.name, charge))
            self.cart.clear()


alice = Customer('Alice', 20)
charlie = Customer('Charlie', 17)
bob = Customer('Bob', 40)

cart1 = Cart(alice)
cart2 = Cart(bob)
cart3 = Cart(charlie)
cart4 = Cart(alice)

shampoo = Item('Dove', 800, False)
soap = Item('Safeguard', 150, False)
pomade = Item('MAC', 1000, False)
toothbrush = Item('Splat', 700, False)
vodka = Item('Ztarskaya', 1200, True)
cigarettes = Item('Marlboro', 350, True)

cart1.add_to_cart(shampoo, 2)
cart1.add_to_cart(pomade, 1)
cart2.add_to_cart(soap, 5)
cart2.add_to_cart(toothbrush, 1)
cart3.add_to_cart(vodka, 1)

assert alice.cart == {shampoo: 2, pomade: 1}
assert bob.cart == {soap: 5, toothbrush: 1}
assert charlie.cart == {}

assert alice.check() == 2600
alice.pay(2600)
assert alice.cart == {}

cart4.add_to_cart(cigarettes, 2)
assert alice.cart == {cigarettes: 2}
alice.pay(700)
assert bob.check() == 1450
bob.pay(1000)
