#!/usr/bin/env python
'''
Impactos Ambientales
---------------------------
Autor: Pedro Luis Lugo Garcia
Version: 1.0
 
Descripcion:
Programa creado para realizar los cálculos del ODP.
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pedro.lugo@unc.edu.ar"
__version__ = "1.0"


import math


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

def validaOdp(compuesto, formula, pesoMolecular, numeroCloro, numeroBromo, constantekOh, constantekCl, constantekO3, constantekNo3):
    
    if (isinstance(compuesto, str) == False or len(compuesto) == 0):
            return "El compuesto no puede estar vacio o nulo"
    if (isinstance(formula, str) == False or len(formula) == 0):
            return "El formula no puede estar vacio o nulo"
    if validarNumero(pesoMolecular) == False or float(pesoMolecular) <= 0:
        return "El peso Molecular no puede estar vacio, nulo, negativo o letras"
    if validarNumero(numeroCloro) == False or int(numeroCloro) < 0:
        return "El número de Cloro del COV no puede estar vacio, nulo, negativo o letras"
    if validarNumero(numeroBromo) == False or int(numeroBromo) < 0:
        return "El número de Bromo del COV no puede estar vacio, nulo, negativo o letras"
    if validarNumero(constantekOh) == False or float(constantekOh) < 0:
            return "La constante kOH no puede estar vacio, nulo, negativo o letras"
    if validarNumero(constantekCl) == False or float(constantekCl) < 0:
        return "La constante kCl no puede estar vacio, nulo, negativo o letras"
    if validarNumero(constantekO3) == False or float(constantekO3) < 0:
        return "La constante kO3 no puede estar vacio, nulo, negativo o letras"
    if validarNumero(constantekNo3) == False or float(constantekNo3) < 0:
        return "La constante kNO3 no puede estar vacio, nulo, negativo o letras"

def calculoTiempo(constantekOh, constantekCl, constantekO3, constantekNo3):
    lista_tiempos = []
    if constantekOh != 0:
        tiempoOh = (1/(2E6 * constantekOh)) / (3600 * 24 * 365)
        
    else:
        tiempoOh = 0
    lista_tiempos.append(tiempoOh)
    if constantekCl != 0:
        tiempoCl = (1/(3.3E4 * constantekCl)) / (3600 * 24 * 365)
        
    else:
        tiempoCl = 0
    lista_tiempos.append(tiempoCl)
    if constantekO3!= 0:
        tiempoO3 = (1/(5E8 * constantekO3)) / (3600 * 24 * 365)
        
    else:
        tiempoO3 = 0
    lista_tiempos.append(tiempoO3)
    if constantekNo3!= 0:
        tiempoNo3 = (1/(7E11 * constantekNo3)) / (3600 * 24 * 365)
        
    else:
        tiempoNo3 = 0
    lista_tiempos.append(tiempoNo3)
   
    acum = 0
    for i in range(len(lista_tiempos)):
        if lista_tiempos[i] !=0:
            acum = acum + 1 / lista_tiempos[i]
    return 1 / acum
    
        
        
        
        
    