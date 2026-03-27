


class Usuario:
    def __init__(self, username, email, password, activo):
        self.usarname = username
        self.email = email
        self.password = password
        self.activo = activo
    def leer(self):
        print(f"nombre:{self.usarname} email: {self.email} activo: {self.activo}")
    def login(self, passw):
        if self.password != passw:
            print("password incorrecto")
        else:
            print("password correcta")
    def desactivar(self):
        self.activo = False


        usuario = Usuario("juanito" , "correo@correo.cl" , "1234" , True)