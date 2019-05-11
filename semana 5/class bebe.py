class Bebe:
    def __init__(self, nombre):
        self.Bebe_nombre = nombre
        self.edad = 0
        self.altura = 0

    def respirar(self):
        print('respira')

    def comer(self, i=0):
       print()

    def llorar(self):
        print('llora')

    def dormir(self):
        print('duerme tarde')

    def crecer(self, e=1, a=1):
        self.edad += e
        self.altura += a


#objeto a crear
mathias = Bebe('bebe')
#asiganr las cualidades del bebe
mathias.comer()
mathias.llorar()
mathias.dormir()
mathias.respirar()
print(mathias.edad, mathias.altura)
mathias.crecer()
print(mathias.edad, mathias.altura)
mathias.crecer(10)
print(mathias.edad, mathias.altura)
mathias.crecer(10,10)
print(mathias.edad, mathias.altura)
#declarar 4 acciones: llorar, respirar, comer, dormir..
#simular un día normal de un bebe



