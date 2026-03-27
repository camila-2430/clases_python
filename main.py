
#clase persona tiene que ser en mayuscula la primera letra y reservada class




class Persona: 
    def __init__(self,nombre, edad, rut):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut

    
    def saludar(self):
        print(f"hola mi nombre es : {self.nombre} y tengo {self.edad}")

    def cumplir_anios(self):
        self.edad +=1
      
    def verificar_rut(self):
        if self.rut == 0:   







#instancia
juanito = Persona("juanito", 34, 1234567893)
carlos = Persona("carlos", 32, 124637752)

print(carlos.saludar())
print(carlos.verificar_rut())
print(carlos.edad())
print(carlos.saludar())
