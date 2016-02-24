# -*- coding: utf-8 -*-

import json
import os


def carga_json():
    with open(ruta_archivo_unidades) as data_file:
        data = json.load(data_file)
    print "¡Unidades cargadas correctamente!"
    return data


ruta_archivo_unidades = "./unidades.json"
arreglo_unidades = carga_json()


def dame_equivalencia(grupo, unidad, unidad2):
    equivalencias = arreglo_unidades['unidades'][grupo]['equivalencias'][unidad]
    return equivalencias[unidad2]


def a_que_grupo_pertenece(unidad_buscada):
    unidades_finales = arreglo_unidades['unidades']
    for grupo in unidades_finales:
        unidades = unidades_finales[grupo]['unidades']
        for unidad in unidades:
            if unidad == unidad_buscada:
                return str(grupo)
    return False


def pide_conversion():
    conversion_deseada = raw_input("¿Qué quieres convertir?\n")
    return conversion_deseada


def es_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False


def corta_oracion(oracion):
    pos_primer_espacio = oracion.find(" ")
    if pos_primer_espacio == -1:
        print "Error: La oración debe llevar espacios; si no, no entiendo."
        return False
    if pos_primer_espacio <= 0:
        print "Error: La oración no puede llevar espacios al inicio."
        return False
    pos_nexo = oracion.find(" a ")
    if pos_nexo == -1:
        print "Error: Recuerda que debes unir las dos unidades con el nexo 'a', por ejemplo: '5 metros a yardas'."
        return False
    numero_unidades = oracion[0:pos_primer_espacio]
    if not es_numero(numero_unidades):
        print "Error: El número de unidades que quieres convertir no es válido."
        return False
    primera_unidad = oracion[pos_primer_espacio + 1: pos_nexo]
    segunda_unidad = oracion[pos_nexo + 3:len(oracion)]
    oracion_cortada = {
        "numero_unidades": numero_unidades,
        "primera_unidad": primera_unidad,
        "segunda_unidad": segunda_unidad
    }
    return oracion_cortada


def main():
    oracion = pide_conversion()
    oracion_cortada = corta_oracion(oracion)
    if oracion_cortada is not False:
        print "Muy bien, la oración es válida."
        primera_unidad = oracion_cortada['primera_unidad']
        segunda_unidad = oracion_cortada['segunda_unidad']
        numero_unidades = oracion_cortada['numero_unidades']
        grupo_unidad1 = a_que_grupo_pertenece(oracion_cortada['primera_unidad'])
        if grupo_unidad1 is False:
            print "Lo siento, pero no reconozco la siguiente unidad: " + oracion_cortada['primera_unidad']
            return
        grupo_unidad2 = a_que_grupo_pertenece(oracion_cortada['segunda_unidad'])
        if grupo_unidad2 is False:
            print "Lo siento, pero no reconozco la siguiente unidad: " + oracion_cortada['segunda_unidad']
            return
        if grupo_unidad1 != grupo_unidad2:
            print "Lo siento, no puedo convertir unidades de diferentes grupos. Ya que " \
                  + "'" + primera_unidad + "'" + " pertenece al grupo " + "'" + grupo_unidad1 + "'" + " mientras que " \
                  + "'"+segunda_unidad + "'"+ " pertenece al grupo " + "'"+grupo_unidad2 + "'."
            return
        print "Perfecto, ambas unidades están registradas."
        equivalencia = dame_equivalencia(grupo_unidad1, primera_unidad, segunda_unidad)
        resultado = equivalencia * float(numero_unidades)
        resultado_string = str(numero_unidades) \
                           + " " \
                           + primera_unidad \
                           + " equivalen a " \
                           + str(resultado) \
                           + " " + segunda_unidad
        lineas = ""
        for x in range(0, len(resultado_string)):
            lineas += "-"

        print lineas
        print resultado_string
        print lineas
        os.system('cls')
        main()
        return True
    print "Error: La oración no es válida"
    return False


main()
