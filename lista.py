from services import Services

class Lista(object):
    
    __services = Services()
    
    def __init__(self,vertices):
        
        self.__lista = []

        for i in range(vertices):
            self.__lista.append([])

    def addAresta(self,profissionais):
        
        for v in profissionais:               
            for w in profissionais:
                if v.getIndice() != w.getIndice(): 
                    self.__lista[v.getIndice()].append([w.getNome(), self.__services.haversine(v.getCoordenadas(),w.getCoordenadas())])
        

    def mostraLista(self,profissionais):
        j = 0
        for i in self.__lista:
            print(str(profissionais[j].getNome()) + " -> " + str(i))
            j = j + 1

    def getLista(self):
        return self.__lista