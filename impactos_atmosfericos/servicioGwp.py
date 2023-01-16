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

def validaGwp(compuesto, formula, pesoMolecular, concentration, opticalPath, constantekOh, constantekCl, constantekO3, constantekNo3):
    
    if (isinstance(compuesto, str) == False or len(compuesto) == 0):
            return "El compuesto no puede estar vacio o nulo"
    if (isinstance(formula, str) == False or len(formula) == 0):
            return "El formula no puede estar vacio o nulo"
    if validarNumero(pesoMolecular) == False or float(pesoMolecular) <= 0:
        return "El peso Molecular no puede estar vacio, nulo, negativo o letras"
    if validarNumero(constantekOh) == False or float(constantekOh) < 0:
            return "La constante kOH no puede estar vacio, nulo, negativo o letras"
    if validarNumero(constantekCl) == False or float(constantekCl) < 0:
        return "La constante kCl no puede estar vacio, nulo, negativo o letras"
    if validarNumero(constantekO3) == False or float(constantekO3) < 0:
        return "La constante kO3 no puede estar vacio, nulo, negativo o letras"
    if validarNumero(constantekNo3) == False or float(constantekNo3) < 0:
        return "La constante kNO3 no puede estar vacio, nulo, negativo o letras"
    if validarNumero(concentration) == False or float(concentration) < 0:
        return "La concentración no puede estar vacio, nulo, negativo o letras"
    if validarNumero(opticalPath) == False or float(opticalPath) < 0:
        return "El paso optico no puede estar vacio, nulo, negativo o letras"


def calculoTimegwp(constantekOh, constantekCl, constantekO3, constantekNo3):
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


def calculoGwp(pesoMolecular, tiempoGlobal, rf_corrected):
    listaGwp = []
    
    listaGwp.append((rf_corrected*(28.97/pesoMolecular)*(1E9/5.135E18)*tiempoGlobal*(1-(math.exp(-20/tiempoGlobal)))) / 2.495E-14)
    
    listaGwp.append((rf_corrected*(28.97/pesoMolecular)*(1E9/5.135E18)*tiempoGlobal*(1-(math.exp(-100/tiempoGlobal)))) / 9.171E-14)
         
    listaGwp.append((rf_corrected*(28.97/pesoMolecular)*(1E9/5.135E18)*tiempoGlobal*(1-(math.exp(-500/tiempoGlobal)))) / 3.217E-13)
    print(listaGwp)
    return listaGwp



    