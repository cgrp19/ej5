import os

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.opc2,
                            3: self.opc3,
                            4: self.opc4,
                            5: self.opc5,
                            0: self.salir
                        }
        
    def opcion(self,op, mPA):   ##mPA == manejador plan de ahorro
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op ==1 or op==2 or op==3 or op==4 or op==5:
            func(mPA)
        else:
            func()

    def opc1 (self, mPA):
        mPA.carga()
        print (str(mPA))

    def opc2(self, mPA):
        mPA.actualizarValor()
        os.system('cls')
        print ('---------->Nuevos Valores<----------\n')
        print (mPA)
    
    def opc3(self, mPA):
        os.system('cls')
        print ('---------->Ver planes menores a un valor de cuota<----------\n')
        aux = int (input ('ingrese valor de cuota: '))
        mPA.verPlanesPorValor(aux)

    def opc4(self, mPA):
        os.system('cls')
        print ('---------->Ver monto total para licitar vehiculo<----------\n')
        aux = int (input ('Ingrese código de plan: '))
        mPA.mostarCantidadLicitar(aux)
    
    def opc5(self, mPA):
        os.system('cls')
        print ('---------->Modificar la cantidad cuotas que debe tener pagas para licitar<----------\n')
        aux = int (input ('Ingrese codigo de plan: '))
        mPA.cambiarCuotas(aux)

    def salir(self):
        print('Saliendo...')