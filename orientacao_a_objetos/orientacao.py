class Restaurante: # Definindo a classe Restaurante
    nome = ''
    ano_de_fundacao = 0
    ativo = False

restaurante = Restaurante() # Instanciando um objeto da classe Restaurante

restaurante.nome = 'Restaurante do Zé' # Atribuindo um valor ao atributo nome
restaurante.ano_de_fundacao = 1990 # Atribuindo um valor ao atributo ano_de_fundacao
restaurante.ativo = True # Atribuindo um valor ao atributo ativo

print(restaurante.nome) 
print(dir(restaurante)) # Exibindo os atributos e métodos do objeto restaurante
print(vars(restaurante)) # Exibindo os atributos e valores do objeto restaurante