#Usando paso de parametros desde consola con argparse
#Para ejecutar desde consola --> rutadearchivo.py parametros posicionales -parametros opcionales
import argparse

parser = argparse.ArgumentParser(description="Paso de parametros")
parser.add_argument("p1", type=str, help="Nombre del usuario")
parser.add_argument("p2", type=int, help="Edad actual")
parser.add_argument("-p3", type=int, help="Años a sumar", default=0)
params = parser.parse_args()
params.p2+=params.p3
print(f"Hola {params.p1}, en {params.p3} años tendrás {params.p2}")
