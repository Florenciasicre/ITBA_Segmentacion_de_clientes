class Razones:

    def __init__(self, cliente, evento):
        self.evento = evento
        self.cliente = cliente
        self.tipo = type(self.cliente).__name__
        self.resolverEvento()
 
    def resolverEvento(self):

        for razon in self.evento:
             if razon['estado'] == 'RECHAZADA':
                 self.razon = razon
                 getattr(self, str(self.razon['tipo']))()

    def ALTA_CHEQUERA(self):
        print(self.tipo)
        match self.tipo:
            case 'Gold':
                print('a')
    
    
    def ALTA_TARJETA_CREDITO(self):
        pass
    
    def COMPRA_DOLAR(self):
        pass
    
    def RETIRO_EFECTIVO_CAJERO_AUTOMATICO(self):
        if self.razon['monto'] > self.razon['cupoDiarioRestante']:
            return f"""El monto a retirar ${self.razon['monto']} 
            supera el cupo diario disponible ${self.razon['cupoDiarioRestante']}"""
        elif self.razon['monto'] > self.razon['saldoEnCuenta']: 
            return f"""El monto a retirar ${self.razon['monto']} 
            supera el monto total de la cuenta ${self.razon['saldoEnCuenta']}"""
    
    def TRANSFERENCIA_ENVIADA(self):
        pass
    def TRANSFERENCIA_RECIBIDA(self):
        pass

    
    
    