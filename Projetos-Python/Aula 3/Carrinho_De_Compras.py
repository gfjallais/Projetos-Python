class Item:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor
    
    
    @property
    def nome(self):
        return self.__nome
    
    
    @property
    def valor(self):
        return self.__valor


class Livro(Item):
    desconto = 3/100
    def __init__(self, nome, valor):
        super().__init__(nome, valor)       
        self.__nome = nome
        self.__valor = valor


class Brinquedo(Item):
    desconto = 5/100
    def __init__(self, nome, valor):
        super().__init__(nome, valor)   
        self.__nome = nome
        self.__valor = valor


class Eletronico(Item):
    desconto = 8/100
    def __init__(self, nome, valor):
        super().__init__(nome, valor)     
        self.__nome = nome
        self.__valor = valor


class CestaCompras:
    def __init__(self):
        self.itens = {}
    

    def adicionar_item(self, item, qtde):
        self.itens[item] = qtde


    def relatorio_final(self):
        soma = 0.0

        for item in self.itens:
            soma += item.valor * self.itens[item] * (1-item.desconto)
        
        print("{:.2f}".format(soma))

        for item in self.itens:
            print(type(item).__name__, item.nome, self.itens[item], "{:.2f}".format(item.valor), 
            "{:.2f}".format(item.valor*self.itens[item]), 
            "{:.2f}".format(item.valor*self.itens[item]*(1-item.desconto)), sep = ', ')