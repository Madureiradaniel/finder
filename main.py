from Pessoa import Pessoa
from lista import Lista
from services import Services


def main():
    
    services = Services()
    lista = Lista(4)

    usuario = Pessoa('daniel',{'latitude': -15.0001, 'longitude': -47.9292 },'developer',0,0)
    
    p1 = Pessoa('daniel',{'latitude': -15.7801, 'longitude': -47.9292 },'developer',0,1)
    p2 = Pessoa('giovanni',{'latitude': -16.6799, 'longitude': -49.255},'developer',0,2)
    p3 = Pessoa('ricardo',{'latitude': -10.6799, 'longitude': -49.255},'developer',0,2)


    lista.addAresta(p1,p2)
    lista.addAresta(usuario,p1)
    lista.addAresta(usuario,p3)
    print(lista.mostraLista())



if __name__ == '__main__':
   main()
