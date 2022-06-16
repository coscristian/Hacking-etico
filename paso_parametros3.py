#Paso de parametros desde consola usando action='store_true' y 'store_false'
#Sirven para almacenar datos booleanos (Los almacenan por defecto, no hay necesidad de darselos como parametro)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--d1', action='store_true')
parser.add_argument('--d2', action='store_false')
params = parser.parse_args()
print(f"Dato 1 --> {params.d1}", f"Dato 2 --> {params.d2}", sep="\n")

