"""Se está pensando en el diseño de un juego que incluye la nave espacial Enterprise. 
En el juego, esta nave tiene un nivel de potencia de 0 a 100, y un nivel de coraza de 0 a 20. La Enterprise 
puede:
--> encontrarse con una pila atómica, en cuyo caso su potencia aumenta en 25.
--> encontrarse con un escudo, en cuyo caso su nivel de coraza aumenta en 10.
--> recibir un ataque, en este caso se especifican los puntos de fuerza del ataque recibido. 
La Enterprise "detiene" el ataque con la coraza, y si la coraza no alcanza, el resto se descuenta de la potencia. 
Por ejemplo si la Enterprise con 80 de potencia y 12 de coraza recibe un ataque de 20 puntos de fuerza,
puede parar solamente 12 con la coraza, 
los otros 8 se descuentan de la potencia. La nave debe quedar con 72 de potencia y 0 de coraza. 
Si la Enterprise no tiene nada de coraza al momento de recibir el ataque, entonces todos los puntos de fuerza del ataque 
se descuentan de la potencia.

La potencia y la coraza tienen que mantenerse en los rangos indicados, por ejemplo, si la Enterprise tien 16 puntos 
de coraza y se encuentra con un escudo, entonces queda en 20 puntos de coraza, no en 26. Tampoco puede quedar negativa la 
potencia, a lo sumo queda en 0. La Enterprise nace con 50 de potencia y 5 de coraza
"""

class Enterprise:
    def __init__(self):
        self.potencia = 50
        self.coraza = 5

    def pila_atomica(self):
        if self.rango_potencia is not True:
            self.potencia += 25
        else: self.potencia = 100
        
    def escudo(self):
        if self.rango_escudo is not True:
            self.coraza += 10
        else: self.escudo = 20

    def rango_potencia(self):
        return self.potencia < 100

    
    def rango_escudo(self):
        return self.escudo < 20
    
    def recibir_ataque(self,daño):
        self.coraza -= daño
        if self.coraza < 0:
            self.potencia += self.coraza
            self.coraza = 0
        self.vida

    def fortaleza_defensiva(self):
        return self.potencia + self.coraza
    
    def necesita_fortalecerse(self):
        return (self.coraza == 0 + self.potencia < 20)

    def fortaleza_ofensiva(self):
        pass

    def vida(self):
        if self.potencia < 0:
            self.potencia = 0
        else: pass

enterprise = Enterprise()
enterprise.pila_atomica()
enterprise.recibir_ataque(14)
enterprise.escudo()

print(enterprise.potencia)
print(enterprise.coraza)
print(enterprise.necesita_fortalecerse())