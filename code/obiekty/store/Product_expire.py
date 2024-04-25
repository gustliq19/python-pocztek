from .Product import Product


class ProductExpire(Product):
    def __init__(self, name, category_name, price, production_year, expire_years):
        super().__init__(name, category_name, price)
        self.expire_years = expire_years
        self.production_year = production_year

    def does_expire(self, current_year):
        return (current_year - self.production_year) >= self.expire_years
