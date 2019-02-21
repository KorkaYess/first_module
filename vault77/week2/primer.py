def cost(weight, kg_price):
    return weight * kg_price

def tax(weight):
    if weight < 10:
        return 0.25
    else:
        return 0.1

def price_after_tax(weight = 30, kg_price = 100):
    return (cost(weight, kg_price) * (1 - tax(weight)))

result = price_after_tax()
print(result)