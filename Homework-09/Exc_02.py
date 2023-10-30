DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    for key in customer:
        if customer.get('discount') == 0:
            return price
        elif not customer.get('discount'):
            price = price * (1-DEFAULT_DISCOUNT)
            return price
        else:
            price = price * (1 - customer.get('discount'))
            return price
        
customer = {"name": "Dima"}
print(get_discount_price_customer(15, customer))
customer = {"name": "Boris", "discount": 0.15}
print(get_discount_price_customer(15, customer))
customer = {'name': 'Olga', 'discount': 0}
print(get_discount_price_customer(15, customer))
# for key in customer:
#     print(key, 'correspond to', customer[key])
