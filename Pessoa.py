class Pessoa(object):

    def __init__(self,nome,coordenadas,profissao,situacao,indice):
        self.__indice = indice
        self.__nome = nome
        self.__coordenadas = coordenadas
        self.__profissao = profissao
        self.__situacao = situacao
    
    def getNome(self):
        return self.__nome
    
    def getCoordenadas(self):
        return self.__coordenadas

    def getProfissao(self):
        return self.__profissao
    
    def getsituacao(self):
        return self.__situacao
        
    def getIndice(self):
       return self.__indice