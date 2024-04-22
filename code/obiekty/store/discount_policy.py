def loyal_customer_discount(order_value):
    return order_value * 0.95


def christmas_discount(order_value):
    if order_value > 100:
        return order_value - 20
    else:
        return order_value


def default_discount_policy(order_value):
    return order_value
