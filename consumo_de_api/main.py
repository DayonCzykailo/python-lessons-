from models import Prato, Bebida, ItemCardapio
from api import Api
from restaurante import Restaurante
import json

def main():
    # prato = Prato('feijoada', 25.0, 'Feijoada completa')
    # bebida = Bebida('Coca-Cola', 5.0, 'Lata 350ml')

    request = Api("https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json")

    get_json = request.get()

    # print(get_json)

    itens = []

    #{'Company': 'Pizza Hut', 'Item': 'Hand Tossed Slices Veggie Lover’s® Large', 'price': 50.63, 'description': 'Sabor exótico que vai te surpreender.'}
    for item in get_json:

        if any(item_list.company == item['Company'] for item_list in itens):
            for item_list in itens:
                if item_list.company == item['Company']:
                    item_list.itens.append(item['Item'])
        else:
            restaurante = Restaurante(company=item['Company'], price=item['price'], description=item['description'])
            restaurante.itens.append(item['Item'])
            itens.append(restaurante)

    # for item in itens:
    #     print(item)
    #     print('-------------------')

    with open('restaurantes.txt', 'w') as file:
        json.dump(itens, file, indent=4,default=lambda k: k.__dict__)
    

        
        


if __name__ == '__main__':
    main()