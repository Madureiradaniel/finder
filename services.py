from math import radians, cos, sin, asin, sqrt
from Pessoa import Pessoa

class Services:
    #calcular km
    def haversine(self, a, b ):
        # Raio da Terra em Km
        r = 6371

        # Converte coordenadas de graus para radianos
        lon1, lat1, lon2, lat2 = map(radians, [ a['longitude'], a['latitude'], b['longitude'], b['latitude'] ] )

        # Formula de Haversine
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        hav = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        km = 2 * r * asin( sqrt(hav) )

        return km
    
    def  subLista(self,listaAdjacencia,usuario,raio,tiposProfissional):       
        
        profissionaisRaio = []
        profissionaisRaio.append(usuario)
        
        for profissional in listaAdjacencia[usuario.getIndice()]:
            if profissional['distancia'] <= raio:
               if profissional['profissional'].getProfissao() in tiposProfissional and profissional['profissional'].getsituacao() == True:
                    profissionaisRaio.append(profissional['profissional'])
                       
        return profissionaisRaio

    def lerProfissionais(self):
        pessoas = []
        usuario = Pessoa('Daniel',-15.0001,-47.9292 ,'usuario',True,0)       
        indice = 1 
        pessoas.append(usuario)

        with open("profissionais") as profissionais:
            for row in profissionais:
                row =row.replace(",", ";")               
                atributos =list(map(str,row.split(";")))            
                pessoa = Pessoa(atributos[0],float(atributos[1]),float(atributos[2]),atributos[3],bool(atributos[4].replace("\n", "")),indice)
                #print(str(pessoa.getIndice()) + pessoa.getNome() +" "+str(pessoa.getProfissao())+ " " +str(pessoa.getCoordenadas())+ " Situacao:" +str(pessoa.getsituacao()))
                pessoas.append(pessoa)
                indice += 1        
        return pessoas

    def MostraProfissionais(self,profissionais): 
        for i in profissionais: 
            if i.getIndice() != 0:
                a = "Disponivel" if i.getsituacao() == True else "Indisponivel"       
                print(str(i.getIndice()) + " "+ i.getNome() + " " +i.getProfissao() + " " + str(a))
