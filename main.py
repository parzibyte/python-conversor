# -*- coding: utf-8 -*-

import json


def __main__():
    if not instrucciones_mostradas:
        muestra_instrucciones()
    oracion = pide_conversion()
    if oracion == "unidades":
        muestra_unidades()
    else:
        if len(oracion) <= 0:
            print "Error: Tienes que escribir lo que quieres convertir."
            __main__()
        oracion_cortada = corta_oracion(oracion)
        if oracion_cortada is not False:
            print "Muy bien, la oracion es valida."
            primera_unidad = oracion_cortada['primera_unidad']
            segunda_unidad = oracion_cortada['segunda_unidad']
            numero_unidades = oracion_cortada['numero_unidades']
            grupo_unidad1 = a_que_grupo_pertenece(primera_unidad)
            if grupo_unidad1 is False:
                print "Lo siento, pero no reconozco la siguiente unidad: " + oracion_cortada['primera_unidad']
                __main__()
            grupo_unidad2 = a_que_grupo_pertenece(segunda_unidad)
            if grupo_unidad2 is False:
                print "Lo siento, pero no reconozco la siguiente unidad: " + oracion_cortada['segunda_unidad']
                __main__()
            if grupo_unidad1 != grupo_unidad2:
                print "Lo siento, no puedo convertir unidades de diferentes grupos. Ya que " \
                      + "'" + primera_unidad + "'" + " pertenece al grupo " + "'" + grupo_unidad1 + "'" + " mientras que " \
                      + "'" + segunda_unidad + "'" + " pertenece al grupo " + "'" + grupo_unidad2 + "'."
                __main__()
            print "Perfecto, ambas unidades estan registradas."
            resultado_string = convertir(grupo_unidad1, primera_unidad, segunda_unidad, numero_unidades)
            lineas = ""
            for x in range(0, len(resultado_string)):
                lineas += "-"
            print lineas
            print resultado_string
            print lineas
            __main__()
            return
    print "Error: La oracion no es valida"
    __main__()
    return


def a_que_grupo_pertenece(unidad_buscada):
    unidades_finales = arreglo_unidades['unidades']
    for grupo in unidades_finales:
        unidades = unidades_finales[grupo]['unidades']
        for unidad in unidades:
            if unidad == unidad_buscada:
                return str(grupo)
    return False


def carga_json():
    with open(ruta_archivo_unidades) as data_file:
        data = json.load(data_file)
    print "Unidades cargadas correctamente."
    return data


def convertir(grupo_unidad1, primera_unidad, segunda_unidad, numero_unidades):
    print "Convirtiendo..."
    if grupo_unidad1 == "Temperatura":
        equivalencia = convertirGrados(primera_unidad, segunda_unidad, numero_unidades)
        resultado = equivalencia
    else:
        equivalencia = dame_equivalencia(grupo_unidad1, primera_unidad, segunda_unidad)
        resultado = equivalencia * float(numero_unidades)
    resultado_string = str(numero_unidades) \
                       + " " \
                       + primera_unidad \
                       + " equivalen a " \
                       + str(resultado) \
                       + " " + segunda_unidad
    return resultado_string


def convertirGrados(primera_unidad, segunda_unidad, numero_unidades):
    numero_unidades = float(numero_unidades)
    if primera_unidad == "grado fahrenheit":
        if segunda_unidad == "grado fahrenheit":
            return numero_unidades
        if segunda_unidad == "grado celsius":
            return (numero_unidades - 32) * (5 / 9)
        if segunda_unidad == "kelvin":
            return ((5 * (numero_unidades - 32)) / 9) + 273.15
    if primera_unidad == "grado celsius":
        if segunda_unidad == "grado fahrenheit":
            return 32 + ((9 / 5) * numero_unidades)
        if segunda_unidad == "grado celsius":
            return numero_unidades
        if segunda_unidad == "kelvin":
            return numero_unidades + 273.15
    if primera_unidad == "kelvin":
        if segunda_unidad == "grado fahrenheit":
            return ((9 * (numero_unidades - 273.15)) / 5) + 32
        if segunda_unidad == "grado celsius":
            return numero_unidades - 273.15
        if segunda_unidad == "kelvin":
            return numero_unidades


def corta_oracion(oracion):
    pos_primer_espacio = oracion.find(" ")
    if pos_primer_espacio == -1:
        print "Error: La oracion debe llevar espacios; si no, no entiendo."
        return False
    if pos_primer_espacio <= 0:
        print "Error: La oracion no puede llevar espacios al inicio."
        return False
    pos_nexo = oracion.find(" a ")
    if pos_nexo == -1:
        print "Error: Recuerda que debes unir las dos unidades con el nexo 'a', por ejemplo: '5 metros a yardas'."
        return False
    numero_unidades = oracion[0:pos_primer_espacio]
    if not es_numero(numero_unidades):
        print "Error: El numero de unidades que quieres convertir no es valido."
        return False
    primera_unidad = oracion[pos_primer_espacio + 1: pos_nexo]
    segunda_unidad = oracion[pos_nexo + 3:len(oracion)]
    oracion_cortada = {
        "numero_unidades": numero_unidades,
        "primera_unidad": primera_unidad,
        "segunda_unidad": segunda_unidad
    }
    return oracion_cortada


ruta_archivo_unidades = "./unidades.json"
arreglo_unidades = carga_json()
instrucciones_mostradas = False


def dame_equivalencia(grupo_unidad1, primera_unidad, segunda_unidad):
    equivalencias = arreglo_unidades['unidades'][grupo_unidad1]['equivalencias'][primera_unidad]
    return equivalencias[segunda_unidad]


def es_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False


def muestra_instrucciones():
    global instrucciones_mostradas
    print "-----------------------------------------"
    print "----------INSTRUCCIONES------------------"
    print "Es importante que prestes atencion, porque"
    print "esto solamente aparecera una vez."
    print "Para convertir, simplemente tienes que es-"
    print "-cribir una oracion compuesta de la sigui"
    print "-ente manera:"
    print "numero de unidades + nombre unidad convertida + 'a' + nombre unidad a convertir"
    print "Aqui tienes unos ejemplos:"
    print "20 metro a yarda"
    print "2 centimetro a pulgada"
    print "NOTA: Por favor escribe en singular, ya que"
    print "el programa no entiende si escribes algo como:"
    print "20 centimetros a pulgadas"
    print "Si en cualquier momento deseas ver las unidades"
    print "que puedo convertir, escribe 'unidades' en lugar"
    print "de la oracion para convertir. ¡GRACIAS!"
    raw_input("Presiona una tecla para continuar...")
    instrucciones_mostradas = True


def muestra_unidades():
    unidades_finales = arreglo_unidades['unidades']
    for grupo in unidades_finales:
        print "--------------------------------------"
        print "Grupo: " + grupo
        unidades = unidades_finales[grupo]['unidades']
        for unidad in unidades:
            print "Unidad: " + unidad


def pide_conversion():
    conversion_deseada = raw_input("Escribe lo que quieres convertir:\n")
    return conversion_deseada










__main__()
