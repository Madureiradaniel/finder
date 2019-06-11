from services import Services
from lista import Lista
from dijkstra import Dijkstra

def main():
    service = Services()
    pessoas = service.lerProfissionais()
    lista = Lista(len(pessoas))
    lista.addArestas(pessoas) 
    #lista.mostraLista(pessoas)
    op = -1
    while op == -1:   

        print("Digite as profissoes que deseja: (separados por virgula)")
        
        profissoes = input("")
        profissoes = str(profissoes).split(",")
        #print(profissoes)

        print("Digite o Raio(KM) para a busca: ")
        raio = float(input(""))
        #print(raio) 
        
        profissionaisDisponiveis = service.subLista(lista.getLista(),pessoas[0],raio,profissoes)
        
        if len(profissionaisDisponiveis) > 1: # maior que pois o usuario esta presente nesta lista
            print("Escolha um ou varios profissionais digitando seu ID: (separados por virgula) ")
            service.MostraProfissionais(profissionaisDisponiveis)
            profissionaisEscolhidos = str(input(""))
            profissionaisEscolhidos = list(map(int, profissionaisEscolhidos.split(",")))
            
            print("Profissionais escolhidos: " + str(profissionaisEscolhidos))   
            # verifica os ids digitados e retorna uma lista com os objetos pessoa referente aos ids
            selecionados = service.getProfissionais(profissionaisEscolhidos,profissionaisDisponiveis) 
            
            #faz um novo grafo somente com os profissionais de acordo com os parametros passados pelo usuario   
            sub_lista = Lista(len(selecionados))
            sub_lista.addArestas(selecionados)
            sub_lista.mostraLista(selecionados)
            
            #sub_lista.mostraLista(profissionaisEscolhidos)
            
            #verifica o menor caminho utilizando o algoritmo dijkstra
            #e retorna o vetor pai e o vetor de custos
            usuario = {'profissional': selecionados[0], 'distancia' : 0} # selecionados[0] -> sempre é o usuario
            dijkstra = Dijkstra(sub_lista.getLista(),usuario,selecionados) 
            dijkstra.melhorCaminho()
            print("Para sair digite '0' | para continuar digite '1' ")
            option = int(input(""))
            op = 0 if option == 0  else -1    
        
        else:
            print ("--Não existe profissionais com esses Parâmetros, tente com outro raio ou Profissão--") 
            print("Para sair digite '0' para continuar digite 1")
            option = int(input(""))  
            op = 0 if option == 0  else -1    

if __name__ == '__main__':
   main()