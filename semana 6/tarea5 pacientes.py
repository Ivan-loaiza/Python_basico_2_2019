lista_enfermedades = ('tos', 'vomito', 'dolor de cabeza', 'mareos')
lista_medicamentos = ('jarabe', 'pastilla', 'tratamiento', 'inyeccion')


agenda = {
    'identificacion':
            {'paciente':12312,
            'nombre':'Bart',
            'apellido':'Simpson',
            'telefono':87264379,
            'direccion':'Casa conde',
            'lista_enfermedades': lista_enfermedades,
            'lista_medicamentos': lista_medicamentos}
}

Carlos = {
    'identificacion':1234115,
    'nombre': 'Carlos',
    'apellido': 'Vazques',
    'telefono':34763722,
    'direccion':'limonal',
    'lista_enfermedades': lista_enfermedades
}

agenda.update(Carlos)

#set investigar sobre lo que hace en si

pass
