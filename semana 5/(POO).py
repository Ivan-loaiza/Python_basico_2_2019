class First:
    pass

a = First()

print(type(a))

class First:
    def __init__(self):
        print('constructor ejecutado')

f = First()

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
#definir el objeto llamado donald
donald = Duck()
#darle las cualidades dice quack y walk..
donald.quack()
donald.walk()
#Crear una class llamada Bebe

class Duck:
    def __init__(self, nombre):
        self.Duck_nombre = nombre

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck')
#nace un pato llamado donald
donald = Duck('donald')
#donald dice quack y camina
donald.quack()
donald.walk()
print('cual es tu nombre?', donald.Duck_nombre)
#'bebe como te llamas?'  me llamo : nombre
