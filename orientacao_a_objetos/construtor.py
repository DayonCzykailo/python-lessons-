class Restaurante:
    restaurantes = [] # meio que uma variavel static

    def __init__(self, nome, ano_de_fundacao, ativo):
        self.nome = nome
        self.ano_de_fundacao = ano_de_fundacao
        self.ativo = ativo
        Restaurante.restaurantes.append(self)

    @classmethod
    def function_random(cls):
        print('Make something...')

    def list_print_all(self):
        for restaurante in self.list_all():
            print(restaurante)

    def list_all(self):
        return Restaurante.restaurantes
    
    def __str__(self): # toString em Python
        return f'Nome: {self.nome}, Ano de fundação: {self.ano_de_fundacao}, Ativo: {self.ativo}'

restaurante = Restaurante('Restaurante do Zé', 1990, True)
restaurante = Restaurante('Restaurante do Carlos', 1980, True)

restaurante.list_print_all()