from Fila import Fila

class Dijkstra:
    
    def __init__(self,grafo,s):
        
        INFINITO = len(grafo)
        self.pai = [-1] * INFINITO
        custo = [INFINITO] * INFINITO

        fila = Fila()
        
        custo[s['profissional'].getIndice()] = 0
        print(custo)
        self.pai[s['profissional'].getIndice()] = s 
        fila.QEUEput(s)

        while fila.QEUEempty() !=0:
            v = fila.QEUEget()
            for p in grafo[v['profissional'].getIndice()]:
                w=p
                if custo[w['profissional'].getIndice()] == INFINITO:
                    self.pai[w['profissional'].getIndice()] = v
                    custo[w['profissional'].getIndice()] = custo[v['profissional'].getIndice()]+p['distancia']
                    fila.QEUEput(w)
                    print(custo) 
                elif custo[w['profissional'].getIndice()] > (custo[v['profissional'].getIndice()]+p['distancia']):
                    self.pai[w['profissional'].getIndice()] = v
                    custo[w['profissional'].getIndice()] = custo[v['profissional'].getIndice()] + p['distancia']                     
                    fila.PQdec(w,custo[v['profissional'].getIndice()] + p['distancia'])
            
        print(custo) 
            
    def mostraPai(self):
        for pai in self.pai:
            print(pai['profissional'].getNome())
