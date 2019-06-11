from services import Services
from lista import Lista

def main():
    service = Services()
    pessoas = service.lerProfissionais()
    lista = Lista(len(pessoas))
    lista.addArestas(pessoas) 
    lista.mostraLista(pessoas)
        
    print("Digite as profissoes que deseja: (separados por virgula)")
    profissoes = input("")
    profissoes = str(profissoes).split(",")
    #print(profissoes)

    print("\nDigite a o Raio para a busca: ")
    raio = float(input(""))
    #print(raio) 
    
    print("Escolha um ou varios profissionais digitando seu ID: (separados por virgula) ")
    profissionaisDisponiveis = service.subLista(lista.getLista(),pessoas[0],raio,profissoes)
    service.MostraProfissionais(profissionaisDisponiveis)
    profissionaisEscolhidos = str(input(""))
    profissionaisEscolhidos = list(map(int, profissionaisEscolhidos.split(",")))
    print(profissionaisEscolhidos)
    
    #sub_lista = Lista(len(profissionaisDisponiveis))
    #sub_lista.addArestas(profissionaisDisponiveis)
    #sub_lista.mostraLista(profissionaisDisponiveis)




if __name__ == '__main__':
   main()