#Paso de parametros desde consola usando el parametro action="store_const"
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--miNombre", action="store_const", const='Cristian')
params = parser.parse_args()
print(params.miNombre)