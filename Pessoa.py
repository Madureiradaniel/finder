class Pessoa(object):

    def __init__(self,nome,latitude,longitude,profissao,situacao,indice):
        self.__indice = indice
        self.__nome = nome
        self.__latitude = latitude
        self.__longitude = longitude
        self.__profissao = profissao
        self.__situacao = situacao
    
    def getNome(self):
        return self.__nome
    
    def getCoordenadas(self):                
        coordenadas = {'latitude' : self.__latitude,'longitude' : self.__longitude}
        return coordenadas

    def getProfissao(self):
        return self.__profissao
    
    def getsituacao(self):
        return self.__situacao
        
    def getIndice(self):
       return self.__indice