
#pilares de la poo
"""

#encapsulacion

class CuentaBancaria:
    def __init__(self, titular , saldo):
        self.titular = titular
        self.__saldo= saldo

    def __str__(self):
        return f"esto es el objeto:{self.titular} y tiene un saldo de:{self.saldo}"

    
    def Depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

                            #10000
    def retirar(self, monto):
        if monto < self.__saldo:
            self.__saldo -= monto
        else:
            print("el retiro no es posible, trabaja mas")



cuanta1 = CuentaBancaria("juanito", 10)
cuenta2 = CuentaBancaria("marcela", 100)

# esto es el objeto <__main__.CuentaBancaria object at

print(cuanta1.retirar(1000))
print(cuenta1)

"""



#herencia

class Vehiculo:
    def __init__(self,marca):
        self.marca = marca

    def moverse(self):
        print("el auto se movio!!!")

class
