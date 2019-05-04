#ejemplo del funcionamiento
#funcion para sumar 2 numeros
#definicion
def mi_suma(a , b):
    return a + b
#posicion
c = mi_suma(1,2)

# nombre
c = mi_suma(a=3, b=4)
# funcion sin parametro
def f():
    a = 9
    b = 0
    print('hola', a, b)
f()
#hacer una funcion que imprima una funcion que las cantidades de filas dadas por un parametro

def mi_triangulo(h):
    for i in range(1, h+1):
        print('*' * i)

mi_triangulo(h=3)

def agregar_contac (nombre, telefono, correo):
    agenda.update({nombre:
                       {'telefono': telefono,
                        'correo': correo}})

    agenda[nombre] = {'telefono': telefono,
                      'correo': correo}


agregar_contac(nombre='felipe',
               telefono='1234123',
               correo='felipe@gmail.com')
print(agenda)

lambda: (lambda a, b: a+b)(3, 4)
x = lambda a, b : a * b
x = (3, 4)