class planAhorro:
    __codPLan: int
    __mod: str
    __ver: str
    __valor: int
    __cuotas = int (60) ## cantidad de cuotas del plan
    __licitar = int (10) 

    def __init__ (self, codigo=0, modelo=None, version=None, valor=0.0):
        self.__codPLan = codigo
        self.__mod = modelo
        self.__ver = version
        self.__valor = valor

#Metodos de clase
    @classmethod
    def cambiarCuotasLicitar(cls, c):
        cls.__licitar = c


    def getCodigo (self):
        return int(self.__codPLan)
    
    def getModelo (self):
        return self.__mod

    def getVersion (self):
        return self.__ver
    
    def getValor (self):
        return int (self.__valor)
    
    def getCuotas (self):
        return int (self.__cuotas)
    
    def getLicitar (self):
        return int(self.__licitar)
    
    def setValor (self, valor):
        self.__valor = valor
        print ('Valor actualizado')