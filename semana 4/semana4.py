mi_dict = {
    'llave1' : 'valor1',
    'llave2' : 'valor2'
}

#opcion 2
otra_dict = dict(llave1 = 'valor1',
                 llave2 = 'valor2')
pass


agenda = {
    'juan perez' : {'telefono':83013040 ,'correo': 'jperez@gmail.com'},
    'carlos rojas' : {'telefono': 87001030, 'correo': 'crojas@hotmail.com'},
    'ana marin': {'telefono': 91787894, 'correo': 'ana@marin.com'}

}
# cuantos contactos hay en agenda
print(len(agenda))

#cuales son los nombres de los contactos
list(agenda.keys())

#imprima la informaciones de cada contacto
for i in agenda:
    print(agenda)


for x in agenda.keys():
    print(x)

for y in agenda.values():
    print(y)

#keys()
for persona in agenda.keys():
    print('nombre: ', persona, 'telefono:', agenda[persona]['telefono'],
          'correo: ', agenda[persona]['correo'])
#items()
for persona, info in agenda.items():
    print('nombre:', [persona],
          'telefono:' ,info['telefono'],
          'correo:',info['correo'])
# agregar a sofia

#opcion 1 : crear diciionario para sofia
sofia = {'telefono': 3333333,
         'correo:': 'sofia@gmail.com'}
agenda['sofia castro'] = sofia
# segunda op :
agenda.update({'sofia alfaro': sofia})
pass

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

