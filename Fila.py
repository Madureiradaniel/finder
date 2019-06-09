class Fila(object):

    def __init__(self):

        self.__dados = []

    def __str__(self):

       return "%s" % (self.__dados)

    def QEUEput(self, elemento):

        self.__dados.append(elemento)

    def QEUEget(self):        
        menor = self.__dados[0]
        for i in self.__dados:                                   
            if i['distancia'] < menor['distancia']:
                menor = i         
        return self.__dados.pop(self.__dados.index(menor))
    
    def PQdec(self,w,custo):

        for elemento in self.__dados:
           if elemento['profissional'].getIndice() == w['profissional'].getIndice():
               self.__dados[self.__dados.index(elemento)]['distancia'] = custo

    def QEUEfree(self):

        del self.__dados[:]
        del self.__dados

    def QEUEempty(self):
        if len(self.__dados) == 0:
            return 0





