App Química Atmosférica (Impactos Ambientales) 📊 🏭
Este es un proyecto de creación de una app para conocer los impactos ambientales (Potencial de Acidificación (AP), Potencial de Creación de Ozono troposferico (POCP), tiempo de residencia atmosférico y Potencial de Calentamiento Global (GWP)) de un compuesto orgánico volatil (COV) en la atmósfera.

Metodologia Experimental
Potencial de Acidificación
La oxidación troposférica de compuestos orgánicos volátiles que contienen Cl, F, N o S en sus estructuras químicas también podría contribuir a la acidificación atmosférica, ya que generalmente producen especies ácidas (de Leeuw, 1993), ácidos carboxílicos, que particularmente llegan al suelo en deposición húmeda. procesos con muy alta capacidad de lavado (de Leeuw, 1993), por lo que el AP viene dado por:

![image](https://github.com/user-attachments/assets/5b9e19c8-1dcc-4faa-8e1d-ba03e7f636bd)


n: El número de átomos de Cl, F, N y S en una molécula.
MSO2 Peso molecular SO2
MCOVs Peso molecular del COV
Potencial de Creación de Ozono Troposferico
Una forma de estudiar la posible formación de Ozono troposférico de un COV en el aire, es a traves del estudio del calculo del POCP

![image](https://github.com/user-attachments/assets/cc07f929-7bfe-42ce-a711-5f9cec320273)


![image](https://github.com/user-attachments/assets/8d639935-2a95-4b05-b0b9-426872f4cb68)


![image](https://github.com/user-attachments/assets/8d1469b6-8c77-4ffb-80ee-b99b89199036)


Tiempo de residencia atmosférico
Uno de los parámetros que dan mucha información acerca de los posibles impactos ambientales de un COV en la atmosfera es el tiempo de residencia atmosferico, el cual relaciona la constante cinética del compuesto con la concentración del oxidante, ya sea, radicales OH*, Cl, NO3 y O3. Asi se conoce si el COV tiene un impacto local, regional o mayor.

Técnias de medición (datos)
FTIR: Espectroscopía Infrarroja con Transformada de Fourier
GC-FID: Cromatografía Gaseosa con Detector de Llama
Pre-requisitos de la app 📋
La app requiere la instalación de las siguientes librerias:

import numpy as np

import csv

import sqlite3

import traceback

import io

import sys

import os

import base64

import json

from datetime import datetime, timedelta

import pandas as pd

import math

from flask import Flask, request, jsonify, render_template, Response, redirect , url_for, session

from flask_sqlalchemy import SQLAlchemy

import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from matplotlib.figure import Figure

import matplotlib.image as mpimg

Estructura de la App Química Atmosférica ⌨
app : El programa app es donde se desarrolla la parte central de la aplicación y llama a las demás funciones, métodos, etc.
impactos : El programa impactos se crea para calcular los diferentes impactos como son: AP, POCP y tiempo de residencia de un COV en la atmosfera.
compuestos: Este programa se crea para determinar las propiedades de compuestos organicos volatiles a estudiar en la atmosfera, para ello crea y se conecta a una base de datos.
parámetros_acidificacion:Programa creado para crear una base datos de potencial de creación de ozono troposférico de compuestos organicos volátiles (COVs) en el aire.
parámetros_ozono: Programa creado para crear una base datos de potenciales de acidificación de un COV teniendo como referencia un grupo de compuestos como el SO2, NO2, NOx, NH3, HCl y HF en el aire.
Datos de entrada de la App 💻
Se debe dar click al boton que dice Datos COV y colocar los datos del compuesto como aparece en la imagen, luego dar click en el boton Ingresar
image

Luego automaticamente la app lleva a la pagina de potencial de acidificacion donde hay que ingresar los datos que alli se piden
image

Al dar click en el boton Calcular arrojara en la parte inferior los resultados de AP
image

El siguiente paso es calcular los POCP para ello debe dar click en el boton de Potencial POCP, ingresar los datos como en pantalla y presionar Calcular
image

image

image

image

Ahora hay que dar click en el boton de tiempo de residencia, ingresar los datos y presionar Calcular
image

image

El ultimo parámetro para calcular es el Potencial de Calentamiento Global (GWP) presionamos el boton GWP e ingresamos los datos. Hay que tener en cuenta, que el archivo de datos para el cálculo del GWP debe estar en formato .csv
image

Al dar click en el boton de Calcular, el programa arroja la siguiente pagina
image

Para obtener los resultados en una sola pagina para una mejor experiencia del usuario y una visión amplia del COV a estudiar, se debe dar click al boton de Estadisticas y el programa arroja la siguiente información
image

image

image

Notas Importantes 📉
El archivo a ingresar para calcular el GWP del compuesto a estudiar, debe estar en formato .csv y en la parte superior de las celdas debe contener cm-1 y abs debido a que el programa lee el archivo tipo diccionario.
![image](https://github.com/user-attachments/assets/5ac0dac7-d803-4ebf-a92f-3251e51eb022)


Los botones como Tablero, Usuario y Perfil no se encuentran habilitados, ésto es porque la app esta diseñada para que otros becarios doctorales puedan mejorar el codigo de la presente app y actualizar las otras funciones que la app puede ofrecer.
Contribución 🚀
Esta app de química atmosferica orientado a los impactos ambientales que un Compuesto Orgánico Volátil (COV) puede ocasionar en la atmósfera, contribuye al estudio que actualmente se esta llevando acabo en los laboratorios: LUQCA de la Universidad Nacional de Córdoba (Argentina) y en BUW de la Universidad de Wuppertal (Alemania) y con la finalidad de que sea un área de investigación (simulaciones, data science, etc) en ambos centros de investigación de quimica atmosferica.

Versión 📌
Versión 1.01

Autor ✒
MSc. Pedro Lugo
Becario Doctoral CONICET-UNC
