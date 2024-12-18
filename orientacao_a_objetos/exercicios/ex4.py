# Desafios

#     Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
#     Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
#     Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
#     Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
#     Crie uma instância da classe e imprima o valor da propriedade titular.
#     Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
#     Crie um método de classe para a conta ClienteBanco.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self) -> str:
        return f'Titular: {self.titular}, Saldo: {self.saldo}'

conta1 = ContaBancaria('João', 1000)
conta2 = ContaBancaria('Maria', 2000)

print(conta1)
print(conta2)

class ContaBancaria:
    def __init__(self, titular, saldo, banco, data, ativo=False):
        self._titular = titular
        self._saldo = saldo
        self._banco = banco
        self._data = data
        self._ativo = ativo

    @property
    def titular(self):
        return self._titular.title()
    
    def ativar_conta(self):
        self._ativo = True

contaBancaria1 = ContaBancaria('João', 1000, 'Banco 1', '01/01/2021')
contaBancaria2 = ContaBancaria('Maria', 2000, 'Banco 2', '02/01/2021')
contaBancaria3 = ContaBancaria('José', 3000, 'Banco 3', '03/01/2021')