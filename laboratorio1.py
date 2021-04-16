#!/usr/bin/python3

# Emilio Javier Rojas Álvarez 2021
# Laboratorio 1
# Se imprimen los números primos menores o iguales a un número n ingresado por el usuario.
# El número n es ingresado como agumento en la línea de comandos o es solicitado al usuario.

import sys


def primos_menores_o_iguales(n):
    "Devuelve los primos menores o iguales a n"

    primos = []  # Array para colocar números primos menores o iguales a n
    count = n  # número que se prueba si es primo o no
    div = 0  # divisor para revisar si count es primo o no

    # Se chequean todos los números de mayor a menor
    while (count > 0):
        div = count - 1
        while (div > 1):
            # Prueba, no debe ser divisible entre ningún número.
            if (count % div == 0):
                break
            div = div - 1  # Siguiente divisor.
            if (div == 1):
                primos.append(count)
        count = count - 1  # Siguiente número.
    if (n >= 2):
        primos.append(2)  # El número 2 es un primo.
    return primos


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
    count = len(primos)
    while (count > 0):
        print(primos[count-1])
        count = count - 1


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
