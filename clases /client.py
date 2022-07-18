from cuenta import Cuenta
from direccion import Direccion

class Client ():
    def __init__(self, data):
       self.nombre = data['nombre']
       self.apellido = data['apellido']
       self.dni = data['dni']
       self.tipo = data['tipo']
       self.direccion = Direccion(data['direccion'])
       self.cuenta = Cuenta()
       print('Se creo el cliente con DNI'+ str(self.dni))

    def puede_crear_chequera(self): return False
    def puede_crear_tarjeta_credito(self): return False
    def puede_comprar_dolar(self): return False 

class Classic(Client):
     def __init__(self, data):
       print('Categoría: Classic')
       super(Classic,self).__init__(data)
       self.cuenta.limite_extraccion_diario = 10000
       self.cuenta.costo_tranferencia = 0.01
       self.cuenta.limite_tranferencia_recibida= 15000

     def puede_crear_chequera(self): return False 

     def puede_comprar_dolar(self): return False 
    
     def puede_crear_tarjeta_credito(self): return False

class Gold(Client):
    def __init__(self, data):
        super(Gold,self).__init__(data)
        self.cuenta.limite_extraccion_diario = -10000
        self.cuenta.costo_tranferencia = 0.05
        self.cuenta.limite_tranferencia_recibida = 500000

    def puede_crear_chequera(self): return True  
    def puede_comprar_dolar(self): return True 
    def puede_crear_tarjeta_credito(self): return True
    
class Black(Client):
    def __init__(self, data):
        print('Categoría: Black')
        super().__init__(data)
        self.cuenta.limite_extraccion_diario = 10000
        self.cuenta.costo_tranferencia = None
        self.cuenta.limite_tranferencia_recibida = None

    def puede_crear_tarjeta_credito(self): return True
    def puede_comprar_dolar(self): return True 
    def puede_crear_chequera(self): return True  