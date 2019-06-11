from Fila import Fila

class Dijkstra:
    
    def __init__(self,grafo,s,profissionaisRaio):
        
        INFINITO = len(grafo)
        self.pai = [-1] * INFINITO
        custo = [INFINITO] * INFINITO

        fila = Fila()
        
        custo[profissionaisRaio.index(s['profissional'])] = 0
        print(custo)
        self.pai[profissionaisRaio.index(s['profissional'])] = s 
        fila.QEUEput(s)

        while fila.QEUEempty() !=0:
            v = fila.QEUEget()
            for p in grafo[profissionaisRaio.index(v['profissional'])]: #v['profissional'].getIndice()
                w=p
                print(w)
                if custo[profissionaisRaio.index(w['profissional'])] == INFINITO:
                    self.pai[profissionaisRaio.index(w['profissional'])] = v
                    custo[profissionaisRaio.index(w['profissional'])] = custo[profissionaisRaio.index(v['profissional'])]+p['distancia']
                    fila.QEUEput(w)
                    print(custo)
                    
                elif custo[profissionaisRaio.index(w['profissional'])] > custo[profissionaisRaio.index(v['profissional'])]+p['distancia']:
                    self.pai[profissionaisRaio.index(w['profissional'])] = v
                    custo[profissionaisRaio.index(w['profissional'])] = custo[profissionaisRaio.index(v['profissional'])] + p['distancia']                     
                    fila.PQdec(w,custo[profissionaisRaio.index(v['profissional'])] + p['distancia'])
            
        print(custo) 
            
    def mostraPai(self,profissionaisRaio):
        aux =0
        for pai in self.pai:
            print( str(profissionaisRaio.index(pai['profissional'])) +  " é pai de " +str(profissionaisRaio.index(profissionaisRaio[aux])))
            aux += 1
        print("\n")
