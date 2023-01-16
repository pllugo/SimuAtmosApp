#!/usr/bin/env python
'''
Impactos Ambientales
---------------------------
Autor: Pedro Luis Lugo Garcia
Version: 1.0
 
Descripcion:
Programa creado para validar los datos ingresados en la plantilla crear.
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pedro.lugo@unc.edu.ar"
__version__ = "1.0"


def validarNumero(numero):
    try:
        if len(numero) == 0:
            return False
        else:
            if isinstance(numero, str) == False:
                return False
            else:
                return True
    except ValueError:
        return False

def isBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return False
    #myString is None OR myString is empty or blank
    return True

def validaAp(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre):
    print(fluor)
    if not compuesto:
        return "El compuesto no puede estar vacio o nulo"

    if not formula:
        return "El formula no puede estar vacio o nulo"
    if not pesoMolecular:
        return "El peso Molecular no puede estar vacio, nulo, negativo o letras"
    if not fluor:
        return "El fluor no puede estar vacio, nulo, negativo o letras"
    if not cloro:
        return "El cloro no puede estar vacio, nulo, negativo o letras"
    if not nitrogeno:
        return "El nitrogeno no puede estar vacio, nulo, negativo o letras"
    if not azufre:
        return "El azufre no puede estar vacio, nulo, negativo o letras"
