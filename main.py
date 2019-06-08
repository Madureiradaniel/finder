from Pessoa import Pessoa
from lista import Lista
from services import Services


def main():
    service = Services()
    usuario = Pessoa('daniel',-15.0001,-47.9292 ,'developer',0,0)    
    p1 = Pessoa('Lucas',-15.7801,-47.9292 ,'developer',0,1)
    p2 = Pessoa('giovanni', -16.6799,-49.255,'developer',0,2)
    p3 = Pessoa('ricardo',-10.6799, -49.255,'developer',0,3)
    p4 = Pessoa('regis',-19.6799, -49.255,'developer',0,4)

    pessoas = [usuario,p1,p2,p3,p4]
    
    lista = Lista(len(pessoas))
    lista.addArestas(pessoas)    
    
    profissionaisRaio = service.subLista(lista.getLista(),usuario,300)
    sub_lista = Lista(len(profissionaisRaio))
    sub_lista.addArestas(profissionaisRaio)
    
    sub_lista.mostraLista(profissionaisRaio)


if __name__ == '__main__':
   main()
