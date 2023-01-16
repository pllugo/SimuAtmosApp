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



def validaPocp(compuesto, formula, pesoMolecular, constantekOh, constantekO3, rendimientoCompuestoConOh, constantekOhProductoNoReactivo, rendimientoproductonoreactivo, claseVoc, region, numeroEnlaces, numeroCarbonos, claseVocP, covsConOzono, numeroEnlacesProducto, covsAromatico):
        

        if isinstance(compuesto, str) == False or len(compuesto) == 0:
            return "El compuesto no puede estar vacio o nulo"
        if (isinstance(formula, str) == False or len(formula) == 0):
            return "El formula no puede estar vacio o nulo"
        if validarNumero(pesoMolecular) == False or float(pesoMolecular) <= 0:
            return "El peso Molecular no puede estar vacio, nulo, negativo o letras"
        if validarNumero(numeroEnlaces) == False or int(numeroEnlaces) < 0:
            return "El número de enlaces del COV no puede estar vacio, nulo, negativo o letras"
        if validarNumero(numeroCarbonos) == False or int(numeroCarbonos) < 0:
            return "El numero de carbonos del COV no puede estar vacio, nulo, negativo o letras"
        if validarNumero(constantekOh) == False or float(constantekOh) < 0:
            return "La constante kOH no puede estar vacio, nulo, negativo o letras"
        if validarNumero(constantekO3) == False or float(constantekO3) < 0:
            return "La constante kO3 no puede estar vacio, nulo, negativo o letras"
        if validarNumero(rendimientoCompuestoConOh) == False or float(rendimientoCompuestoConOh) < 0:
            return "El rendimiento con radicales OH no puede estar vacio, nulo, negativo o letras"
        if validarNumero(constantekOhProductoNoReactivo) == False or float(constantekOhProductoNoReactivo) < 0:
            return "La constante kOH del producto no reactivo no puede estar vacio, nulo, negativo o letras"
        if validarNumero(rendimientoproductonoreactivo) == False or float(rendimientoproductonoreactivo) < 0:
            return "El rendimiento del producto no reactivo no puede estar vacio, nulo, negativo o letras"
        if isinstance(claseVoc, str) == False or len(claseVoc) == 0:
            return "El tipo de COV no puede estar vacio, nulo, negativo o letras"
        if isinstance(region, str) == False or len(region) == 0:
            return "La región no puede estar vacio, nulo, negativo o letras"
        if isinstance(claseVocP, str) == False or len(claseVocP) == 0:
            return "El tipo de COV para el producto no puede estar vacio, nulo, negativo o letras"
        if isinstance(covsConOzono, str) == False or len(covsConOzono) == 0:
            return "El tipo de COV para el producto no puede estar vacio, nulo, negativo o letras"    
        if validarNumero(numeroEnlacesProducto) == False or int(numeroEnlacesProducto) < 0:
            return "El número de enlaces para el producto no puede estar vacio, nulo, negativo o letras" 
        if isinstance(covsAromatico, str) == False or len(covsAromatico) == 0:
            return "El número de enlaces para el producto no puede estar vacio, nulo, negativo o letras"
        
        
        
        
    
