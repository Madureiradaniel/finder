from services import Services

class Lista(object):
    
    __services = Services()
    
    def __init__(self,vertices):
        
        self.__lista = []

        for i in range(vertices):
            self.__lista.append([])

    def addAresta(self,v,w):
        
        self.__lista[v.getIndice()].append([w,self.__services.haversine(v.getCoordenadas(),w.getCoordenadas())])
        

    def mostraLista(self):
        j = 0
        for i in self.__lista:
            print(str(j) + " -> " + str(i))
            j = j + 1

    def getLista(self):
        return self.__lista