# Exercícios

#     Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
#     Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
#     Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
#     Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
#     Altere o valor do atributo nome para 'Bistrô'.
#     Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
#     Verifique se a categoria da instância restaurante_pizza é 'Fast Food'. ?????
#     Mude o estado da instância restaurante_pizza para ativo.
#     Imprima no console o nome e a categoria da instância restaurante_praca.

class Restaurante: # Definindo a classe Restaurante
    nome = ''
    restaurante_praca = '',
    categoria = ''
    ano_de_fundacao = 0
    ativo = False

    getActive = lambda self: 'ativo' if self.ativo else 'inativo'

restaurante = Restaurante() # Instanciando um objeto da classe Restaurante

restaurante.nome = 'Restaurante do Zé' # Atribuindo um valor ao atributo nome
restaurante.restaurante_praca = 'Italiana' # Atribuindo um valor ao atributo categoria
restaurante.categoria = "Bistrô" # Atribuindo um valor ao atributo categoria
restaurante.ano_de_fundacao = 1990 # Atribuindo um valor ao atributo ano_de_fundacao
restaurante.ativo = True # Atribuindo um valor ao atributo ativo


pizza_place = Restaurante()
pizza_place.nome = 'Pizza Place'
pizza_place.categoria = 'Fast Food'
pizza_place.ativo = True

if restaurante_pizza.categoria == 'Fast Food':
    print('Categoria Fast Food')
else:
    print('Categoria não Fast Food')

print(f'Nome: {restaurante.nome} Categoria: {restaurante.restaurante_praca}')




print(restaurante.getActive()) # Exibindo se o restaurante está ativo ou inativo
print(dir(restaurante)) # Exibindo os atributos e métodos do objeto restaurante