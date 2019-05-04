
#ejemplos de lambda
x = lambda a : a + 1
x(10)
# crear funcion lambda sin parametros
(lambda : print('hola')) ()

(lambda : 1+1) ()

suma = lambda x, y : x + y
resta = lambda x, y : x - y
multiplique = lambda x, y : x * y
divide = lambda x,y : x/y
import math
potencia = lambda x, y : math.pow(x, y)
raiz = lambda x, y : math.pow(x, 1/y)

x = 3

y = 2

lista_funciones = [suma, resta, multiplique,divide,potencia,raiz]
for mi_funcion in lista_funciones:
    print('resultado=', mi_funcion(x,y))

calculadora = {
    'suma' : suma,
    'resta' : resta,
    'multiplique' : multiplique,
    'divide' : divide
    'raiz' : raiz
}

#usando dict
print('usando dict')
for f in calculadora.values():
    print('resultado=', f(x,y))

