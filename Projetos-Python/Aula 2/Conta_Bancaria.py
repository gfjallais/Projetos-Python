class Conta:
    
    def __init__(self, numero):
        self.__numero = numero
        self.__saldo = 0.0
    
    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor


class ContaCorrente(Conta):
    def __init__(self, numero, taxa):
        super().__init__(numero)
        self.taxa = taxa
    
    def cobrar_taxa(self):
        self.sacar(self.taxa)

class ContaPoupanca(Conta):
    def __init__(self, numero, juros):
        super().__init__(numero)
        self.juros = juros
    
    def aplicar_juros(self):
        self.depositar(self.saldo * self.juros)