from .Order import Order
from .TaxCalculator import TaxCalculator


class ExpressOrder(Order):

    EXPRESS_ORDER_FEE = 15

    def __init__(self, delivery_date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delivery_date = delivery_date

    @property
    def total_price(self):
        total_price = 0
        for order_element in self._order_elements:
            total_price += order_element.value + TaxCalculator.calculate_tax_for_element(order_element)
        return self.discount_policy(total_price) + ExpressOrder.EXPRESS_ORDER_FEE
        # return super().total_price + ExpressOrder.EXPRESS_ORDER_FEE

    def __str__(self):
        to_print = ""
        to_print += f"{'-' * 20}\n"
        to_print += f"EKSPRESOWE ZAMÓWIENIE:\n"
        to_print += f"Zamawiający: {self.orderer_first_name} {self.orderer_last_name}\n"
        to_print += f"Elementy zamówienia:\n"
        for order_element in self._order_elements:
            to_print += "\t" + str(order_element)

        to_print += f"Data dostarczenia: {self.delivery_date}\n"
        to_print += f"Wartość całkowita: {self.total_price:.2f} zł BRUTTO (w tym opłata {ExpressOrder.EXPRESS_ORDER_FEE} zł za eksresowe zamówienie)\n"
        to_print += f"{'-' * 20}\n"

        return to_print
