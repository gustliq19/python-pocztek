class DiscountPolicy:
    @staticmethod
    def apply_discount(order_value):
        return order_value


class PercentageDiscount(DiscountPolicy):
    def __init__(self, discunt_percentage):
        self.discount_percentage = discunt_percentage

    def apply_discount(self, order_value):
        return order_value * (1 - self.discount_percentage / 100)


class AbsoluteDiscount(DiscountPolicy):
    def __init__(self, discount_value):
        self.discount_value = discount_value

    def apply_discount(self, order_value):
        order_discounted_value = order_value - self.discount_value
        if order_discounted_value < 0:
            order_discounted_value = 0
        return order_discounted_value
