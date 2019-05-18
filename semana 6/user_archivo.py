f = open('mis datos.txt')
lines = f.readlines()

from os import path
ruta_archivo = path.join('directorio', 'archivo.txt')

archivo = open(ruta_archivo)
contenido = archivo.read()
archivo.close()
contenido

# Se abre el archivo para escritura con el modo 'w'
archivo = open('texto.txt', 'w')
# se escriben algunas líneas
archivo.write('primera linea\n')
archivo.write('segunda linea\n')
# Y se cierra el archivo para que el sistema actulice la información en disco
archivo.close()

with open('data.txt', 'w') as f:
    f.write('Hello\n')
'''
%ls data.txt

 Volume in drive C is OS
 Volume Serial Number is D69D-F564

 Directory of C:\Users\ecsa

02/28/2019  07:31 AM                 7 data.txt
               1 File(s)              7 bytes
               0 Dir(s)  80,039,895,040 bytes free

% echo data.txt

data.txt
'''

with open('mis datos.txt', 'w') as f:
    f.write('hello\n')


pass