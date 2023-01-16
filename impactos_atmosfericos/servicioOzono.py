#!/usr/bin/env python
'''
Impactos Ambientales
---------------------------
Autor: Pedro Luis Lugo Garcia
Version: 1.0
 
Descripcion:
Programa creado para realizar los cálculos del POCP.
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pedro.lugo@unc.edu.ar"
__version__ = "1.0"


import math


def buscarParametro(claseCov, region, vectorCov, vectorEuropa, vectorUsa):
    resultado = 0
    for i in range(len(vectorCov)):
        if claseCov == vectorCov[i]:
            if region == "europa":
                resultado = vectorEuropa[i]
            else:
                if region == "usa":
                    resultado = vectorUsa[i]
    return resultado


def parametroA(claseCov, region):
    vectorA = ["aliphatics", "aromatics with 0 alkyl substituents", "aromatics with 1 alkyl substituents",
				"aromatics with 2 alkyl substituents", "aromatics with 3 alkyl substituents"]
    vectorEuropa = [100.0, 66.0, 130.0, 173.0, 206.0]
    vectorUsa = [154.0, 25.0, 320.0, 427.0, 509.0]
    return buscarParametro(claseCov, region, vectorA, vectorEuropa, vectorUsa)


def parametroB(region):
    resultado = 0
    if region == "europa":
        resultado = 4
    else:
        if region == "usa":
            resultado = 1
    return resultado


def parametroAlfa(region):
    resultado = 0
    if region == "europa":
        resultado = 0.56
    else:
        if region == "usa":
            resultado = 0.37
    return resultado
    
def parametroC(region):
    resultado = 0
    if region == "europa":
        resultado = 0.0038
    else:
        if region == "usa":
            resultado = 0.0041
    return resultado

def parametroBeta(region):
    resultado = 0
    if region == "europa":
        resultado = 2.7
    else:
        if region == "usa":
            resultado = 2.7
    return resultado

def parametroD(claseCov, region):
    resultado = 0
    if region == "europa" and claseCov == "aliphatics":
        resultado = 0.38
    else:
        if region == "usa" and claseCov == "aliphatics":
            resultado = 0.25
    return resultado


def parametroEpsilon(claseCov, region):
    resultado = 0
    if region == "europa" and claseCov == "aliphatics":
        resultado = 0.16
    else:
        if region == "usa" and claseCov == "aliphatics":
            resultado = 0.18
    return resultado


def parametroP(covsFotolizan, region):
    vectorA = ["aldehydes/ketones", "alpha-dicarbonyls", "cycloketones"]
    vectorEuropa = [14, 67, 0, 0]
    vectorUsa = [10, 124, 0, 0]
    return buscarParametro(covsFotolizan, region, vectorA, vectorEuropa, vectorUsa)


def parametroE(covsConOzono, region):
    resultado = 0
    if region == "europa" and covsConOzono == "alkenes/unsaturated oxygenates":
        resultado = 20.9
    else:
        if region == "usa" and covsConOzono == "alkenes/unsaturated oxygenates":
            resultado = 22
    return resultado


def parametroLambda(covsConOzono, region):
    resultado = 0
    if region == "europa" and covsConOzono == "alkenes/unsaturated oxygenates":
        resultado = 0.043
    else:
        if region == "usa" and covsConOzono == "alkenes/unsaturated oxygenates":
            resultado = 0.15
    return resultado


def parametroQ(covAromatico, region):
    vectorA = ["benzaldehydes/styrenes", "hydroxyarenes"]
    vectorEuropa = [74, 41]
    vectorUsa = [80, 0]
    return buscarParametro(covAromatico, region, vectorA, vectorEuropa, vectorUsa)


def calculoGammaS(numeroEnlaces, pesoMolecular):
    return (numeroEnlaces / 6) * (28.05 / pesoMolecular)

def calculoR(numeroEnlaces, constantekOh, region):
    return (1 - (1 / ((constantekOh / 6.91E-13) * (6 / numeroEnlaces) * parametroB(region) + 1)))

def calculoF(claseCov, region, constantekOh, constantekOhProductoNoReactivo, rendimientoProductoNoReactivo, numeroEnlaces, numeroEnlacesProductos):
    if constantekOhProductoNoReactivo < 2E-12:
        return 1
    else:
        return pow(((numeroEnlaces - (rendimientoProductoNoReactivo * numeroEnlacesProductos)) / numeroEnlaces), parametroD(claseCov, region) * (1 - (1E12 * constantekOhProductoNoReactivo / 2) * 1E12 * pow(constantekOh, parametroEpsilon(claseCov, region))))

def calculoS(numeroCarbonos, region):
    resultado = math.e**(-1 * pow(parametroC(region) * numeroCarbonos, parametroBeta(region)))
    resultado2 = 1 - parametroAlfa(region)
    return resultado2 * resultado + parametroAlfa(region)

def calculoRo3(claseCov, region, constantekO3, rendimientoCompuestoConOh):
    resultadoRo3 = 0
    resultadoE = parametroE(claseCov, region)
    if resultadoE != 0:
        resultadoLambda = parametroLambda(claseCov, region)
        miu = pow((constantekO3 / 1.55E-18) * (rendimientoCompuestoConOh / 0.98), resultadoLambda)
        return pow(resultadoE, miu)
    else:
        return resultadoRo3

def calcularPocp(claseCov, region, pesoMolecular, constantekOh, numeroEnlaces, numeroCarbonos, constantekOhProductoNoReactivo, rendimientoProductoNoReactivo,  numeroEnlacesProducto, claseCovP, covsConOzono, covAromatico, rendimientoCompuestoConOh):
    potencialPocp = (parametroA(claseCov, region) * calculoGammaS(int(numeroEnlaces), float(pesoMolecular)) * calculoR(int(numeroEnlaces), float(constantekOh), region) * calculoS(int(numeroCarbonos), region) * calculoF(claseCov, region, float(constantekOh), float(constantekOhProductoNoReactivo), float(rendimientoProductoNoReactivo), int(numeroEnlaces), int(numeroEnlacesProducto))) + parametroP(claseCovP, region) + calculoRo3(covsConOzono, region, constantekOhProductoNoReactivo, rendimientoCompuestoConOh) + parametroQ(covAromatico, region)
    return potencialPocp
    