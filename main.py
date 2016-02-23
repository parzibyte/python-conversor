#!/usr/bin/env python
# -*- coding: utf-8 -*-


def imprime_opciones():
    print "Elige:"
    print "1 - Energia"
    print "1 - Energia"


def pide_conversion():
    conversion_deseada = raw_input("¿Qué quieres convertir?")
    return conversion_deseada


def corta_oracion(oracion):
    print "La oración que recibo es: " + oracion
    pos_primer_espacio = oracion.find(" ")
    pos_segundo_espacio = oracion.find(" ", pos_primer_espacio+1, len(oracion))
    pos_tercer_espacio = oracion.find(" ", pos_segundo_espacio+1, len(oracion))
    numero_unidades = oracion[0:pos_primer_espacio]
    primera_unidad = oracion[pos_primer_espacio + 1: pos_segundo_espacio]
    print "La posición del primer espacio es: " + str(pos_primer_espacio)
    print "La posición del segundo espacio es: " + str(pos_segundo_espacio)
    print "La posición del tercer espacio es: " + str(pos_tercer_espacio)
    print "El número es: " + "'" + numero_unidades + "'"
    print "La primera unidad es: " + "'"  + primera_unidad + "'"


def main():
    corta_oracion("5 metros a pulgadas")


main()
