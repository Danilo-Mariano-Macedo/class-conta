# Crie um sistema de gerenciamento de contas bancárias em Python usando herança e polimorfismo. O sistema 
# deve incluir as seguintes classes:

# A classe base "Conta " deve ter atributos para o número da conta, o titular da conta e o saldo.
# Ela deve incluir métodos para depósitos, saques e exibição do saldo atual.

# A classe "ContaCorrente " herda de "Conta " e inclui atributos específicos, como taxa de manutenção e 
# limite de cheque especial. Deve sobrescrever o método de saque para considerar o limite de cheque 
# especial, se necessário.

# A classe "ContaPoupanca " também herda de "Conta " e inclui atributos específicos, como taxa de juros. 
# Ela deve ter um método para calcular e adicionar juros ao saldo. 
# Crie um método chamado resumo que pode ser chamado em qualquer objeto de conta (ContaCorrente ou ContaPoupanca).

# Esse método resumo irá exibir um resumo das informações da conta, incluindo o tipo de conta (corrente ou 
# poupança), o número da conta, o titular da conta e o saldo atual. Teste de Funcionalidade: Crie um 
# programa principal que demonstre o uso dessas classes. Crie instâncias de contas correntes e poupanças, 
# realize depósitos, saques, adicione juros e chame o método resumo para cada conta.

# Criando classe Conta
class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor): # Método 
        self.saldo += valor
        print(f'Depósito de R$ {valor} realizado com sucesso.')

    def sacar(self, valor):
        if self.saldo >= valor: # Se o saldo na conta for maior que o saque desejado...
            self.saldo -= valor # Então o saque pode ser realizado
            print(f'Saque de R$ {valor} realizado com sucesso.')
        else:
            print(f'Saldo insuficiente para saque.')

    def exibir_saldo(self):
        print(f'Saldo atual: R$ {self.saldo}') # self.saldo irá exibir o saldo restante

    def resumo(self):
        print(f'Tipo de conta: {self.__class__.__name__}') # Apresentando se a conta é corrente ou poupança
        print(f'Número da conta: {self.numero}')
        print(f'Titular da conta: {self.titular}')
        print(f'Saldo atual: R$ {self.saldo}')

class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo, taxa_manutencao, limite_cheque_especial):
        super().__init__(numero, titular, saldo) # Atributos da class Conta
        self.taxa_manutencao = taxa_manutencao # Atributo da classa Conta_corrente
        self.limite_cheque_especial = limite_cheque_especial # Atributo da classa Conta_corrente

    def sacar(self, valor):
        if self.saldo + self.limite_cheque_especial >= valor: # Se a soma de valores de saldo e limite de cheuqe especial forem maiores que o valor desejado a sacar...
            self.saldo -= valor # Então o saque é permitido
            print(f'Saque de R$ {valor} realizado com sucesso.')
        else:
            print('Saldo insuficiente para saque.')

class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo, taxa_juros):
        super().__init__(numero, titular, saldo) # Atributos da class Conta
        self.taxa_juros = taxa_juros # Atributo da classa Conta_corrente

    def adicionar_juros(self):
        juros = self.saldo * (self.taxa_juros / 100) # Cálculo do juros para dar rendimento a conta
        self.saldo += juros # soma do juros a conta poupança
        print(f'Juros de R$ {juros} adicionados com sucesso')

if __name__ == '__main__':
    # Criando contas
    conta_corrente1 = ContaCorrente(2394, 'Paulo Passos', 1000, 20, 500)
    conta_poupança1 = ContaPoupanca(4326, 'Maria Meireles', 7000, 1)

    # Fazendo depósitos
    conta_corrente1.depositar(500)
    conta_poupança1.depositar(1000)

    # Fazendo saques
    conta_corrente1.sacar(1000)
    conta_poupança1.sacar(200)

    # Acrescentnado juros
    conta_poupança1.adicionar_juros()

    # Exibindo os resumos das contas
    conta_corrente1.resumo()
    conta_poupança1.resumo()