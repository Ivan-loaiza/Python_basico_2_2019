# esto es un ejemplo de creacion de listas

mis_frutas = [ 'fresas', 'manzan', 'mango', 'pera', 'naranja', 'piña']

pass

frutas = [ 'piña', 'naranja', 'sandia']
verduras = [ 'tomates', 'papas', 'cebollas', 'ajos']
carnes = [ 'mortadela', 'pollo', 'costilla de cerdo']
limpieza = [ 'jabon', 'cloro', 'shampo']

lista_de_compras = [frutas,verduras,carnes,limpieza]

pass
#cuantos articulos voy a comprar
mi_lista = [ ]
for categoria in lista_de_compras:
    mi_lista.extend(categoria)
    print(mi_lista)
print(len(mi_lista))
# agregar fruta(mango) y verdura(chile)#

verduras.append('chile')
frutas.append('mango')

print(lista_de_compras)
#otra forma de cuantos articulos voy a comprar

cantidad = 0
for categoria in lista_de_compras:
    cantidad += len(categoria)
print(cantidad)
#utilizando pasos 1,2,4*********** verduras NO
verduras.clear()
print(lista_de_compras)