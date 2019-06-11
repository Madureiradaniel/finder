from Fila import Fila

class Dijkstra:
    
    def __init__(self,grafo,s,profissionaisRaio):
        
        INFINITO = len(grafo)
        self.__pai = [-1] * INFINITO
        self.__custo = [INFINITO] * INFINITO
        self.__profissionaisRaio = profissionaisRaio

        fila = Fila()
        self.__custo[profissionaisRaio.index(s['profissional'])] = 0
        print(self.__custo)
        self.__pai[profissionaisRaio.index(s['profissional'])] = s 
        fila.QEUEput(s)

        while fila.QEUEempty() !=0:
            v = fila.QEUEget()
            for p in grafo[profissionaisRaio.index(v['profissional'])]: #v['profissional'].getIndice()
                w=p
                if self.__custo[profissionaisRaio.index(w['profissional'])] == INFINITO:
                    self.__pai[profissionaisRaio.index(w['profissional'])] = v
                    self.__custo[profissionaisRaio.index(w['profissional'])] = self.__custo[profissionaisRaio.index(v['profissional'])]+p['distancia']
                    fila.QEUEput(w)
                    # print(self.__custo)
                    
                elif self.__custo[profissionaisRaio.index(w['profissional'])] > self.__custo[profissionaisRaio.index(v['profissional'])]+p['distancia']:
                    self.__pai[profissionaisRaio.index(w['profissional'])] = v
                    self.__custo[profissionaisRaio.index(w['profissional'])] = self.__custo[profissionaisRaio.index(v['profissional'])] + p['distancia']                     
                    fila.PQdec(w,self.__custo[profissionaisRaio.index(v['profissional'])] + p['distancia'])
            
        print(self.__custo)
         
    def melhorCaminho(self):
     
       

        return 0


    def mostraPai(self):
        aux =0
        for pai in self.__pai:
            print( str(self.__profissionaisRaio.index(pai['profissional'])) +  " é pai de " +str(self.__profissionaisRaio.index(self.__profissionaisRaio[aux])))
            aux += 1
        print("\n")
