# Calcular el factorial de una lista ordenada de numeros, los numeros se iran ingresando como parametros
# desde la consola
# Usar la funcion sum, por defecto se debe hallar el valor maximo de el grupo de numeros
#Al usar nargs='*' los valores ingresados como parametros se van agregando a una lista
import argparse
import numpy as np
from functools import reduce

parser = argparse.ArgumentParser()
parser.add_argument('-nums', type=int, nargs='*', help = 'Ingresa numeros enteros')
parser.add_argument('-fact', dest='factorial', action='store_const', const=np.prod, default=max)
params = parser.parse_args()
print(f"Conjunto de numeros --> {params.nums}")
print(f"Factorial de {params.nums[-1]} --> {params.factorial(params.nums)}")
