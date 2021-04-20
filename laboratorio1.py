#!/usr/bin/python3

# Emilio Javier Rojas Álvarez 2021
# Laboratorio 1
# Se imprimen los números primos menores o iguales a un número n ingresado por el usuario.
# El número n es ingresado como argumento en la línea de comandos o es solicitado al usuario.
#
# Disponible en:
# https://github.com/stompy-lizard/Laboratorio1

import sys
import math

def primos_menores_o_iguales(n):
    "Devuelve los primos menores o iguales a n"

    primos = []  # Array para colocar números primos menores o iguales a n.

    # Se chequean todos los números.
    for nCheck in range(2, n+1):
        if (esPrimo(nCheck)):
            primos.append(nCheck)
    return primos


def esPrimo(n):
    "Chequea si un número es primo o no"

    # Casos iniciales
    if (n == 2 or n == 3):
        return True
    div = 2
    # Check de primos
    while (div < 1+math.ceil(math.sqrt(n))):
        if (n % div == 0):
            break
        div = div + 1
        if (div == 1+math.ceil(math.sqrt(n))):
            return True
    return False

def obtener_n():
    "Devuelve el valor de n ingresado por el usuario"

    try:
        # Se intenta obtener argumento de la línea de comandos y paresearlo como entero.
        n = int(sys.argv[1])
    except IndexError:
        # Si no existe argumento, se solicita número al usuario.
        # Se solicita hasta que pueda ser parseado como un entero.
        while (True):
            try:
                n = int(input("Ingrese el número: "))
                break
            except ValueError:
                print("Debe ingresar un número entero.")
    except ValueError:
        # Si el argumento no es un entero, se indica el error.
        # Además se devuelve 0 para finalizar el programa.
        n = 0
        print("El argumento debe ser un número entero.")
        print("Para ayuda ejecutar:\n\t%s -h" % sys.argv[0])
    return n

def main():
    "Obtiene n, los números primos menores o iguales a n e imprime estos números"
    primos = primos_menores_o_iguales(obtener_n())
    maxCount = len(primos)
    for idx in range(0, maxCount):
        print(primos[idx])

if (len(sys.argv) > 1 and (sys.argv[1] == "-h")):
    # imprimir ayuda si se encuentra la bandera -h
    print("Laboratorio 1")
    print("\tSe imprimen los números primos menores o iguales a un número n ingresado por el usuario.")
    print("\tEl número n es ingresado como agumento en la línea de comandos o es solicitado al usuario.")
    print("Uso:")
    print("\t%s n" % sys.argv[0])
    print("\tDonde n es un número entero. Si se llama sin argumento, se solicitará al usuario.")
    print("Ejemplos:")
    print("\t%s" % sys.argv[0])
    print("\t%s 100" % sys.argv[0])
else:
    # ejecutar programa si no se encuentra la bandera de ayuda -h
    main()
