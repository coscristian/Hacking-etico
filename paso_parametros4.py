#Paso de parametros desde consola usando action='append'
#Sirve para agregar los parametros a una lista
#El primer parametro de add_argument es el nombre corto que se le da al parametro opcional para ir agregando
#El segundo parametro de add_argument es el nombre que se le da a lista que será atributo de params
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--numeros', action='append', type=int)
params = parser.parse_args()

print(params.numeros)
print(type(params.numeros))