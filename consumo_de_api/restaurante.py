import json
#{'Company': 'Pizza Hut', 'Item': 'Hand Tossed Slices Veggie Lover’s® Large', 'price': 50.63, 'description': 'Sabor exótico que vai te surpreender.'}
class Restaurante:
    
    def __init__(self, company, price, description):
        self.company = company
        self.price = price
        self.itens = []
        self.description = description

    # def __str__(self):
    #     return f"Company: {self.company}, Price: {self.price}, Description: {self.description}, Itens: {self.itens}"
    
    def get_json(self) -> str:
        return json.dumps(self.__dict__)
