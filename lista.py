from services import Services

class Lista(object):
    
    __services = Services()
    
    def __init__(self,vertices):
        
        self.__lista = []

        for i in range(vertices):
            self.__lista.append([])

    def addArestas(self,pessoas):
        # faz uma ligaçao entre todas as pessoas presentes no vertice
        for v in pessoas:               
            for w in pessoas:
                if v.getIndice() != w.getIndice(): 
                    self.__lista[v.getIndice()].append({ 'profissional' : w ,'distancia' : self.__services.haversine(v.getCoordenadas(),w.getCoordenadas())}) # adiciona o vertice com o peso da aresta
                    
    def mostraLista(self,pessoas):
        j = 0
        for i in self.__lista:
            print(str(pessoas[j].getNome()) + " -> " + str(i))
            j = j + 1

    def getLista(self):
        return self.__lista