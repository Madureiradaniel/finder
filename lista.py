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
                    self.__lista[pessoas.index(v)].append({ 'profissional' : w ,'distancia' : self.__services.haversine(v.getCoordenadas(),w.getCoordenadas())}) # adiciona o vertice com o peso da aresta
                    
    def mostraLista(self,pessoas):
        
        aux=0
        for i in self.__lista:
            print(end="\n")
            print(pessoas[aux].getNome() + "--> ", end="")
            for j in i:
                print(j['profissional'].getNome() +", " + str(j['distancia'])+", "+ str(j['profissional'].getProfissao()) +" KM --> ", end="")                
            aux+=1
        print("\n")  

    def getLista(self):
        return self.__lista