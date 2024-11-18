# Exercícios

#     Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
#     Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
#     Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
#     Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
#     Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro = Carro('Fusca', 'Azul', 1970)

class Restaurante:
    def __init__(self, nome, categoria, fundation, address , ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.fundation = fundation
        self.address = address
        self.ativo = ativo
    
    def __str__(self) -> str:
        return f'Nome: {self.nome}, Categoria: {self.categoria}'

class Cliente:
    def __init__(self, nome, idade, cpf, endereco):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco

cliente1 = Cliente(nome='João', idade=20, cpf='123.456.789-00', endereco='Rua 1')
cliente2 = Cliente('Maria', 30, '987.654.321-00', 'Rua 2')
cliente3 = Cliente('José', 40, '456.789.123-00', 'Rua 3')