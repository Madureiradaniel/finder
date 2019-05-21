class Fila(object):

    def __init__(self):

        self.__dados = []

    def __str__(self):

       return "%s" % (self.__dados)

    def QEUEput(self, elemento):

        self.__dados.append(elemento)

    def QEUEget(self):

        return self.__dados.pop(0)

    def QEUEfree(self):

        del self.__dados[:]
        del self.__dados

    def addInicioDaFila(self,elemento):

        self.__dados.insert(0,elemento)

    def QEUEempty(self):

        if len(self.__dados) == 0:
            return 0

    def getFila(self):

        filaAux = str(self.__dados).replace("[", "")
        filaAux = filaAux.replace("]","")
        if filaAux != '':
            filaAux = filaAux.split(",")
            filaAux = list(map(int,filaAux))
        else:
            filaAux =[]

        return filaAux




