"""
Nombre: generarPi.py
Propósito: Obtener el valor de Pi hasta n decimales
Autor: Pradipta (geekpradd)
Algoritmo: Algoritmo de Chudnovsky
Licencia: MIT

Dependencias del módulo:

Math proporciona cálculo rápido de raíces cuadradas
Decimal proporciona el tipo de dato Decimal que es mucho mejor que Float
sys es necesario para establecer la profundidad de recursión.
"""
from __future__ import print_function
import math, sys
from decimal import *
getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)

python2 = sys.version_info[0] == 2
if python2:
	input = raw_input

def factorial(n):
	"""
	Devuelve el Factorial de un número usando recursión

	Parámetros:
	n -- Número del cual obtener el factorial
	"""
	if not n:
		return 1
	return n*factorial(n-1)


def getIteratedValue(k):
	"""
	Devuelve las iteraciones según lo establecido en el Algoritmo de Chudnovsky.
	k iteraciones dan k-1 lugares decimales. Como necesitamos k lugares decimales,
	hacemos que las iteraciones sean igual a k+1
	
	Parámetros:
	k  -- Número de dígitos decimales a obtener
	"""
	k = k+1
	getcontext().prec = k
	sum=0
	for k in range(k):
		first = factorial(6*k)*(13591409+545140134*k)
		down = factorial(3*k)*(factorial(k))**3*(640320**(3*k))
		sum += first/down 
	return Decimal(sum) 

def getValueOfPi(k):
	"""
	Devuelve el valor calculado de Pi usando el valor iterado del bucle
	y algunas divisiones según lo establecido en el Algoritmo de Chudnovsky

	Parámetros:
	k -- Número de dígitos decimales hasta los cuales se debe calcular el valor de Pi
	"""
	iter = getIteratedValue(k)
	up = 426880*math.sqrt(10005)
	pi = Decimal(up)/iter 
	
	return pi

def shell():
	"""
	Función de consola para crear el Shell interactivo.
	Se ejecuta solo cuando __name__ == __main__, es decir, cuando el script se llama directamente

	Sin valor de retorno ni parámetros
	"""
	print ("Bienvenido a la Calculadora de Pi. En el shell a continuación, ingrese el número de dígitos hasta los cuales se debe calcular el valor de Pi o ingrese quit para salir")

	while True:
		print (">>> ", end='')
		entry = input()
		if entry == "quit":
			break
		if not entry.isdigit():
			print ("No ingresaste un número. Intenta de nuevo")
		else:
			print (getValueOfPi(int(entry)))

if __name__=='__main__':
	shell()