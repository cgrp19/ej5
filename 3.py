import csv
import os
from clasePlanAhorro import planAhorro

class manejadorPlanAhorro:
    __listaPA = []

    def __str__(self):
        s = ""
        for i in range (len(self.__listaPA)):
            s += str(self.__listaPA[i].getCodigo()) + ',' + str(self.__listaPA[i].getModelo()) + ',' + str(self.__listaPA[i].getVersion()) + ',' + str(self.__listaPA[i].getValor()) + ',' + str(self.__listaPA[i].getCuotas()) + ',' + str(self.__listaPA[i].getLicitar()) + '\n'
        return s

    def calcularValorCuota(self, i):
        return int ((self.__listaPA[i].getValor() / self.__listaPA[i].getCuotas()) + self.__listaPA[i].getValor() * 0.10)

    def carga (self):
        path = './planes.csv'
        archivo = open (path, 'r')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            codigo = fila [0]
            modelo = fila[1]
            version = fila[2]
            valor = fila[3]
            pa = planAhorro(codigo, modelo, version, valor)
            self.__listaPA.append(pa)
        if len (self.__listaPA) > 0:
            print ('Carga Lista!')
            print ()
        else: print ('Error en la carga')

    def actualizarValor (self):
        for i in range (len(self.__listaPA)):
            os.system('cls')
            print ('---------->Actualización de precios<----------')
            print(f'''
-> Código de plan: {self.__listaPA[i].getCodigo()}
-> Modelo vehículo: {self.__listaPA[i].getModelo()}
-> Version vehículo: {self.__listaPA[i].getVersion()}
''')
            xValor = int (input ('-> Ingrese nuevo valor para el vehículo: '))
            self.__listaPA[i].setValor(xValor)
            os.system('pause')

    def verPlanesPorValor(self, v): ## v == valor codigo de cuota a buscar
        for i in range (len(self.__listaPA)):   #valor de prueba 487.317
            vCuota = self.calcularValorCuota(i)
            if vCuota < v:
                print (f'''
-> Código de plan: {self.__listaPA[i].getCodigo()}
-> Modelo vehículo: {self.__listaPA[i].getModelo()}
-> Version vehículo: {self.__listaPA[i].getVersion()}
-----------------------------------------------------------''')
                
    def mostarCantidadLicitar (self, v): ## Cantidad de cuotas para licitar vehiculo
        for i in range (len (self.__listaPA)):
            if v == self.__listaPA[i].getCodigo():
                c = self.calcularValorCuota(i)
                print (f'El monto total a pagar para licitar "{self.__listaPA[i].getModelo()}, {self.__listaPA[i].getVersion()}" es: $ {c * self.__listaPA[i].getLicitar()}')

    def cambiarCuotas(self, c): ## c == codigo de plan
        for i in range (len (self.__listaPA)):
            if c == self.__listaPA[i].getCodigo():
                aux = int (input ('Ingrese nuevo cantidad de cuotas para licitar: '))
                self.__listaPA[i].cambiarCuotasLicitar(aux)
                print (f'Se cambió la cantidad de cuotas con exito')