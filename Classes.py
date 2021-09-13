class Ponto2D:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

class Retangulo:
    def __init__(self, esq_sup, dir_inf):
        self.__esq_sup = esq_sup
        self.__dir_inf = dir_inf
    
    @property
    def esq_sup(self):
        return self.__esq_sup
    @esq_sup.setter
    def esq_sup(self, ponto):
        self.__esq_sup = ponto
    @esq_sup.deleter
    def esq_sup(self):
        del self.__esq_sup
    
    @property
    def dir_inf(self):
        return self.__dir_inf
    @dir_inf.setter
    def dir_inf(self, ponto):
        self.__dir_inf = ponto
    @dir_inf.deleter
    def dir_inf(self):
        del self.__dir_inf
    @property
    def width(self):
        return self.dir_inf.x - self.esq_sup.x
    @property
    def height(self):
        return self.esq_sup.y - self.dir_inf.y

    def calcularArea(self):
        return abs(self.esq_sup.x - self.dir_inf.x) * (self.esq_sup.y - self.dir_inf.y)
    
    def calcularIntersecao(self, ret):
        if (ret.esq_sup.x > self.dir_inf.x or ret.dir_inf.x < self.esq_sup.x):
            return None
        if (ret.dir_inf.y > self.esq_sup.y or ret.esq_sup.y < self.dir_inf.y):
            return None
        else:
            return (min(ret.dir_inf.x, self.dir_inf.x) - max(ret.esq_sup.x, self.esq_sup.x)) * (min(ret.esq_sup.y, self.esq_sup.y) - max(ret.dir_inf.y, self.dir_inf.y))