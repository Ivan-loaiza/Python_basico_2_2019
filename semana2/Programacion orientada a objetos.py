class Duck:
    def __init__(self, nombre):
        self.duck_nombre = nombre
    def quack(self):
        print('Quaaack!')
    def walk(self):
        print('Walks like a duck.')

donald = Duck('donald')
#donal dice quack y camina
donald.quack()
donald.walk()
print('cual es tu nombre?', donald.duck_nombre)
