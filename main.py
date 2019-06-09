from Pessoa import Pessoa
from lista import Lista
from services import Services
from dijkstra import Dijkstra

def main():
    service = Services()
    usuario = Pessoa('Daniel',-15.0001,-47.9292 ,'developer',0,0)    
    p1 = Pessoa('Lucas',-15.8801,-47.9292 ,'developer',0,1)
    p2 = Pessoa('Giovanni', -16.8799,-49.255,'developer',0,2)
    p3 = Pessoa('Ricardo',-10.6799, -49.255,'developer',0,3)
    p4 = Pessoa('Regis',-19.6799, -49.255,'developer',0,4)
    p5 = Pessoa('Lucio',-19.6799, -49.255,'developer',0,5)


    pessoas = [usuario,p1,p2,p3,p4,p5]
    
    lista = Lista(len(pessoas))
    lista = lista.getLista()

    lista[0].append({'profissional' : p2, 'distancia' : 7 })
    lista[0].append({'profissional' : p4, 'distancia' : 4 })
    lista[0].append({'profissional' : p3, 'distancia' : 2 })

    lista[1].append({'profissional' : p2, 'distancia' : 0 })

    lista[2].append({'profissional' : p4, 'distancia' : 1 })

    lista[3].append({'profissional' : p4, 'distancia' : 1 })
    lista[3].append({'profissional' : p5, 'distancia' : 3 })

    lista[4].append({'profissional' : p1, 'distancia' : 4 })
    lista[4].append({'profissional' : p5, 'distancia' : 1 })

    lista[5].append({'profissional' : p1, 'distancia' : 2 })


    # lista.addArestas(pessoas)    
    # print("Lista 1")
    # lista.mostraLista(pessoas)
    # print("\n")
    # profissionaisRaio = service.subLista(lista.getLista(),usuario,270)

    # sub_lista = Lista(len(profissionaisRaio))
    # sub_lista.addArestas(profissionaisRaio)
    
    # print("Lista 2")
    # sub_lista.mostraLista(profissionaisRaio)

    usuario = {'profissional': usuario, 'distancia' : 0}
    dj = Dijkstra(lista,usuario)
    dj.mostraPai()
  
if __name__ == '__main__':
   main()
