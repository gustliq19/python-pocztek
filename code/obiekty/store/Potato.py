class Potato:
    def __init__(self, species_name, size, kg_price):
        self.species_name = species_name
        self.size = size
        self.kg_price = kg_price

    def calculate_price(self, kg_amount):
        return self.kg_price * kg_amount

    def print(self):
        print(f"Gatunek: {self.species_name} | Rozmiar: {self.size} | Cena za kg: {self.kg_price}")

    def __repr__(self):
        return f"<{str(self.__class__)[1:-1]}, species_name='{self.species_name}', size='{self.size}', kg_price={self.kg_price}>"
