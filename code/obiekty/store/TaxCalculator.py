class TaxRates:
    FRUITS_VEGETABLES = 0.05
    FOOD = 0.08
    ALL = 0.2


class TaxCalculator:

    @staticmethod
    def calculate_tax_for_element(order_element):
        category_name = order_element.product.category_name
        tax_rate = 0

        if category_name == "Owoce i warzywa":
            tax_rate = TaxRates.FRUITS_VEGETABLES
        elif category_name == "Jedzenie":
            tax_rate = TaxRates.FOOD
        else:
            tax_rate = TaxRates.ALL

        return tax_rate * order_element.calculate_value()
