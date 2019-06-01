#En una carrera de vehículos se tiene una la línea de salida:
#Un camión
#Un tractor
#un sedan
#Un bus
#Cada uno de ellos tienen un rendimiento de avance en metros diferente según sea su tipo:
#Un camión: 2 * (fuerza del motor) + 1
#Un tractor: log(base 2) (fuerza del motor)
#un sedan: 3 * (fuerza del motor)**2
#Un bus: 5 * (fuerza del motor)
#Donde las unidades de (fuerza del motor) son generadas aleatoriamente en un rango del 0 al 9.
import random as rdm
class fuerza_del_motor:
    camion = 2 * ('fuerza_del_motor') + 1
    tractor = log(base 2)and('fuerza del motor')
    sedan = 3 * ('fuerza del motor') **2
    bus = 5 * ('fuerza_del_motor')

    def __init__(self, vehiculo):
        self.vehiculo = vehiculo

velo_camion = lambda x, y : 2 * (fuerza_del_motor) + 1
velo_tractor = lambda x, y : 2 + (fuerza_del_motor)
velo_sedan = lambda x, y : 3 * (fuerza_del_motor) ** 2
velo_bus = lambda x, y : 5 * (fuerza_del_motor)

carrera_vehiculos = [velo_bus, velo_camion, velo_sedan,velo_tractor]
for mi_funcion in carrera_vehiculos:
    print('resultado= ', mi_funcion(x,y))



'''
Resultados esperados
Primer y segundo lugar

Eficiencia de avance máxima por vehículo

Número de intentos por vehículo

Requerimientos de desarrollo
Escrito en Python (Sea en cualquier editor como Pycharm o Jupyter Notebook)

Utilización de los conceptos de clases, herencia, creación de funciones lambda y funciones creadas por el desarrollador.

Sobrecarga de métodos

Envio a pantalla el estado de la carrera

Para el reporte y la obtención de resultados DEBE utilizarse Pandas DataFrames
'''