class FechaHora:
    __dia = 0
    __mes = 0
    __year = 0
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__(self, v1 = 0000, v2 = 00, v3 = 00, v4 = 00, v5 = 00, v6 = 00):
        self.__dia = v1
        self.__mes = v2
        self.__year = v3
        self.__hora = v4
        self.__minutos = v5
        self.__segundos = v6

    def Mostrar(self):
        print(f"{self.__dia}/{self.__mes}/{self.__year} - {self.__hora}:{self.__minutos}:{self.__segundos}")

    def Hora(self, v4 = 12, v5 = 30, v6 = 00):
        self.__dia = 0
        self.__mes = 0
        self.__year = 0
        self.__hora = v4
        self.__minutos = v5
        self.__segundos = v6

    def getSegundos(self):
        return int(self.__segundos)

    def getMinutos(self):
        return int(self.__minutos)

    def getHoras(self):
        return int(self.__hora)

    def getDias(self):
        return int(self.__dia)

    def getMeses(self):
        return int(self.__mes)

    def getYears(self):
        return int(self.__year)

    def __add__(self, other):
        print(type(other))
        if type(self) == type(other):
            cont = 0
            d1 =  self.__segundos + other.getSegundos()
            while d1 > 59:
                d1 - 60
                cont = cont + 1
            d2 = self.__minutos + other.getMinutos() + cont
            cont = 0
            while d2 > 59:
                d2 - 60
                cont = cont + 1
            d3 = self.__hora + other.getHoras() + cont
            cont = 0
            while d3 > 23:
                d3 - 24
                cont = cont + 1
            if self.__year % 4 == 0 and self.__year % 100 == 0:
                d5 = self.__mes
                d4 = self.__dia + other.getDias() + cont
                cont = 0
                if self.__mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                    while d4 > 31:
                        d4 - 30
                        cont = cont + 1
                if self.__mes == 4 or 6 or 9 or 11:
                    while d4 > 30:
                        d4 - 29
                        cont = cont + 1
                if self.__mes == 2:
                    while d4 > 29:
                        d4 - 28
                        cont = cont + 1
                d5 = self.__mes + other.getMeses() + cont
                cont = 0
                while d5 > 12:
                    d5 - 12
                    cont = cont + 1
                d6 = self.__year + other.getYears() + cont
                cont = 0
            else:
                d5 = self.__mes
                d4 = self.__dia + other.getDias() + cont
                cont = 0
                if self.__mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                    while d4 > 31:
                        d4 - 30
                        cont = cont + 1
                if self.__mes == 4 or 6 or 9 or 11:
                    while d4 > 30:
                        d4 - 29
                        cont = cont + 1
                if self.__mes == 2:
                    while d4 > 28:
                        d4 - 27
                        cont = cont + 1
                d5 = self.__mes + other.getMeses() + cont
                cont = 0
                while d5 > 12:
                    d5 - 12
                    cont = cont + 1
                d6 = self.__year + other.getYears() + cont
                cont = 0

            return (d4, d5, d6, d3, d2, d1)

    def __sub__(self, other):
        if type(self) == type(other):
            cont = 0
            d1 = self.__segundos - other.getSegundos()
            while d1 < 1:
                d1 + 60
                cont = cont + 1
            d2 = self.__minutos - other.getMinutos() + cont
            cont = 0
            while d2 < 1:
                d2 + 60
                cont = cont + 1
            d3 = self.__hora - other.getHoras() + cont
            cont = 0
            while d3 < 1:
                d3 + 24
                cont = cont + 1
            if self.__year % 4 == 0 and self.__year % 100 == 0:
                d5 = self.__mes
                d4 = self.__dia + other.getDias() - cont
                cont = 0
                if self.__mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                    while d4 < 1:
                        d4 + 31
                        cont = cont + 1
                if self.__mes == 4 or 6 or 9 or 11:
                    while d4 < 1:
                        d4 + 30
                        cont = cont + 1
                if self.__mes == 2:
                    while d4 < 0:
                        d4 + 29
                        cont = cont + 1
                d5 = self.__mes + other.getMeses() - cont
                cont = 0
                while d5 < 1:
                    d5 + 12
                    cont = cont + 1
                d6 = self.__year + other.getYears() - cont
                cont = 0
            else:
                d5 = self.__mes
                d4 = self.__dia + other.getDias() - cont
                cont = 0
                if self.__mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                    while d4 > 31:
                        d4 - 30
                        cont = cont + 1
                if self.__mes == 4 or 6 or 9 or 11:
                    while d4 < 1:
                        d4 + 30
                        cont = cont + 1
                if self.__mes == 2:
                    while d4 < 1:
                        d4 + 28
                        cont = cont + 1
                d5 = self.__mes + other.getMeses() - cont
                cont = 0
                while d5 < 1:
                    d5 + 12
                    cont = cont + 1
                d6 = self.__year - other.getYears() - cont
                cont = 0

            return (d4, d5, d6, d3, d2, d1)

    def __gt__(self, other):
        fechaMay = 0
        condicion = False
        print(type(other))
        if type(self) == type(other):
            if self.__year != other.getYears() and condicion == False:
                condicion = True
                if self.__year > other.getYears():
                    fechaMay = 1
                else:
                    fechaMay = 2
            elif self.__mes != other.getMeses() and condicion == False:
                condicion = True
                if self.__mes > other.getMeses():
                    fechaMay = 1
                else:
                    fechaMay = 2
            elif self.__dia != other.getDias() and condicion == False:
                condicion = True
                if self.__dia > other.getDias():
                    fechaMay = 1
                else:
                    fechaMay = 2
            elif self.__hora != other.getHoras() and condicion == False:
                condicion = True
                if self.__hora > other.getHoras():
                    fechaMay = 1
                else:
                    fechaMay = 2
            elif self.__minutos != other.getMinutos() and condicion == False:
                condicion = True
                if self.__minutos > other.getMinutos():
                    fechaMay = 1
                else:
                    fechaMay = 2
            elif self.__segundos != other.getSegundos() and condicion == False:
                condicion = True
                if self.__segundos > other.getSegundos():
                    fechaMay = 1
                else:
                    fechaMay = 2
            return(fechaMay)