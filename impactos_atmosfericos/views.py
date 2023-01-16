from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .validar import validaAp
from .validarPocp import validaPocp
from django.views.generic import TemplateView
from .servicioOzono import *
from .servicioOdp import *
from .servicioGwp import *
import pandas as pd
import csv
from .servicioTiempo import *

# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')



def listaap(request):
    listadoPotencialesAp = Acidificacion.objects.all()

    return render(request, 'acidificacion/lista.html', {'listadoPotencialesAp': listadoPotencialesAp})


def crearAp(request):
    if request.method == 'POST':
        compuesto = str(request.POST['compuesto'])

        formula = str(request.POST['formula'])
        pesoMolecular = str(request.POST['pesoMolecular'])
        fluor = str(request.POST['fluor'])
        cloro = str(request.POST['cloro'])
        nitrogeno = str(request.POST['nitrogeno'])
        azufre = str(request.POST['azufre'])
        respuesta = validaAp(
            compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)

        try:
            if int(fluor) >= 0 and int(cloro) >= 0 and int(nitrogeno) >= 0 and int(azufre) >= 0:

                potencialap = (64.066 / float(pesoMolecular)) * \
                    ((int(fluor) + int(cloro) + int(nitrogeno) + 2*int(azufre)) / 2)
                Acidificacion(compuesto=compuesto, formula=formula, pesoMolecular=pesoMolecular, fluor=fluor,
                              cloro=cloro, nitrogeno=nitrogeno, azufre=azufre, potencialap=potencialap).save()
                messages.success(
                    request, "Exito!! Ha registrado el compuesto exitosamente")
                return redirect('/')
            else:
                messages.error(request, "Error, existen halogenos negativos")
                return render(request, 'acidificacion/crear.html')

        except:

            #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
            messages.error(request, respuesta)
            return render(request, 'acidificacion/crear.html')

    else:

        return render(request, 'acidificacion/crear.html')


def edicionAp(request, id):
    covs = Acidificacion.objects.get(id=id)
    return render(request, 'acidificacion/editar.html', {'covs': covs})


def editarAp(request):
    #covs = Acidificacion.objects.get(id=id)
    id = int(request.POST['id'])
    covs = Acidificacion.objects.get(id=id)
    if request.POST:

        compuesto = str(request.POST['compuesto'])

        formula = str(request.POST['formula'])
        pesoMolecular = str(request.POST['pesoMolecular'])
        fluor = str(request.POST['fluor'])
        cloro = str(request.POST['cloro'])
        nitrogeno = str(request.POST['nitrogeno'])
        azufre = str(request.POST['azufre'])
        respuesta = validaAp(
            compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)

        if respuesta == None:

            potencialap = (64.066 / float(pesoMolecular)) * \
                ((int(fluor) + int(cloro) + int(nitrogeno) + 2*int(azufre)) / 2)
            covs.compuesto = compuesto
            covs.formula = formula
            covs.pesoMolecular = pesoMolecular
            covs.fluor = fluor
            covs.cloro = cloro
            covs.nitrogeno = nitrogeno
            covs.azufre = azufre
            covs.potencialap = potencialap
            covs.save()
            messages.success(
                request, "Exito!! Ha editado el compuesto exitosamente")
            return redirect('/')
        else:
            messages.error(request, respuesta)
            return render(request, 'acidificacion/editar.html', {'covs': covs})

    else:

        return render(request, 'acidificacion/editar.html', {'covs': covs})


def eliminarAp(request, id):
    cov = Acidificacion.objects.get(id=id)
    cov.delete()
    listadoPotencialesAp = Acidificacion.objects.all()
    return render(request, 'acidificacion/lista.html', {'listadoPotencialesAp': listadoPotencialesAp})


def displayAp(request):
    listadoPotencialesAp = Acidificacion.objects.all()
    otracosa = Acidificacion.objects.all().values()
    df = pd.DataFrame(otracosa)
    df2 = df['potencialap'].tolist()
    df3 = df['compuesto'].tolist()
    print(df3)
    print(df2)
    diccionario = {
        'df3': df3,
        'df2': df2
    }
    listaNueva = []
    for listAp in listadoPotencialesAp:
        listaNueva.append(listAp.potencialap)
    return render(request, 'acidificacion/dashboard.html', context = diccionario)


def listaPocp(request):
    listadoPotencialesPocp = Ozono.objects.all()

    return render(request, 'ozono/lista.html', {'listadoPotencialesPocp': listadoPotencialesPocp})


def crearPocp(request):
    if request.method == 'POST':
        compuesto = str(request.POST['compuesto'])

        formula = str(request.POST['formula'])
        pesoMolecular = str(request.POST['pesoMolecular'])

        constantekOh = str(request.POST['constantekOh'])
        constantekO3 = str(request.POST['constantekO3'])
        region = str(request.POST['region'])

        rendimientoCompuestoConOh = str(
            request.POST['rendimientoCompuestoConOh'])
        constantekOhProductoNoReactivo = str(
            request.POST['constantekOhProductoNoReactivo'])
        rendimientoProductoNoReactivo = str(
            request.POST['rendimientoProductoNoReactivo'])
        claseCov = str(request.POST['claseCov'])
        claseCovP = str(request.POST['claseCovP'])
        covsConOzono = str(request.POST['covsConOzono'])
        numeroEnlacesProducto = str(request.POST['numeroEnlacesProducto'])
        numeroEnlaces = str(request.POST['numeroEnlaces'])
        numeroCarbonos = str(request.POST['numeroCarbonos'])
        covsAromatico = str(request.POST['covsAromatico'])

        respuesta = validaPocp(compuesto, formula, pesoMolecular, constantekOh, constantekO3, rendimientoCompuestoConOh, constantekOhProductoNoReactivo,
                               rendimientoProductoNoReactivo, claseCov, region, numeroEnlaces, numeroCarbonos, claseCovP, covsConOzono, numeroEnlacesProducto, covsAromatico)

        try:
            if float(pesoMolecular) >= 0 and int(numeroEnlaces) >= 0 and int(numeroCarbonos) >= 0 and float(constantekOh) >= 0 and float(constantekO3) >= 0 and float(rendimientoCompuestoConOh) >= 0 and float(constantekOhProductoNoReactivo) >= 0 and float(rendimientoProductoNoReactivo) >= 0 and int(numeroEnlacesProducto) >= 0:

                potencialPocp = calcularPocp(claseCov, region, pesoMolecular, constantekOh, numeroEnlaces, numeroCarbonos, constantekOhProductoNoReactivo,
                                             rendimientoProductoNoReactivo, numeroEnlacesProducto, claseCovP, covsConOzono, covsAromatico, rendimientoCompuestoConOh)
                print(potencialPocp)
                Ozono(compuesto=compuesto, formula=formula, pesoMolecular=pesoMolecular, constantekOh=constantekOh, constantekO3=constantekO3, region=region, rendimientoCompuestoConOh=rendimientoCompuestoConOh, constantekOhProductoNoReactivo=constantekOhProductoNoReactivo,
                      rendimientoProductoNoReactivo=rendimientoProductoNoReactivo, claseCov=claseCov, claseCovP=claseCovP, covsConOzono=covsConOzono, numeroEnlaces=numeroEnlaces, numeroCarbonos=numeroCarbonos, covsAromatico=covsAromatico, numeroEnlacesProducto=numeroEnlacesProducto, potencialPocp=potencialPocp).save()
                messages.success(
                    request, "Exito!! Ha registrado el compuesto exitosamente")
                return redirect('/')
            else:
                messages.error(request, respuesta)
                return render(request, 'ozono/crear.html')
        except:

            #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
            messages.error(request, respuesta)
            return render(request, 'ozono/crear.html')

    else:

        return render(request, 'ozono/crear.html')


def edicionPocp(request, id):
    covs = Ozono.objects.get(id=id)
    return render(request, 'ozono/editar.html', {'covs': covs})


def editarPocp(request):
    #covs = Acidificacion.objects.get(id=id)
    id = int(request.POST['id'])
    covs = Ozono.objects.get(id=id)
    if request.POST:

        compuesto = str(request.POST['compuesto'])

        formula = str(request.POST['formula'])
        pesoMolecular = str(request.POST['pesoMolecular'])

        constantekOh = str(request.POST['constantekOh'])
        constantekO3 = str(request.POST['constantekO3'])
        region = str(request.POST['region'])

        rendimientoCompuestoConOh = str(
            request.POST['rendimientoCompuestoConOh'])
        constantekOhProductoNoReactivo = str(
            request.POST['constantekOhProductoNoReactivo'])
        rendimientoProductoNoReactivo = str(
            request.POST['rendimientoProductoNoReactivo'])
        claseCov = str(request.POST['claseCov'])
        claseCovP = str(request.POST['claseCovP'])
        covsConOzono = str(request.POST['covsConOzono'])
        numeroEnlacesProducto = str(request.POST['numeroEnlacesProducto'])
        numeroEnlaces = str(request.POST['numeroEnlaces'])
        numeroCarbonos = str(request.POST['numeroCarbonos'])
        covsAromatico = str(request.POST['covsAromatico'])

        respuesta = validaPocp(compuesto, formula, pesoMolecular, constantekOh, constantekO3, rendimientoCompuestoConOh, constantekOhProductoNoReactivo,
                               rendimientoProductoNoReactivo, claseCov, region, numeroEnlaces, numeroCarbonos, claseCovP, covsConOzono, numeroEnlacesProducto, covsAromatico)

        if respuesta == None:
            try:
                if float(pesoMolecular) >= 0 and int(numeroEnlaces) >= 0 and int(numeroCarbonos) >= 0 and float(constantekOh) >= 0 and float(constantekO3) >= 0 and float(rendimientoCompuestoConOh) >= 0 and float(constantekOhProductoNoReactivo) >= 0 and float(rendimientoProductoNoReactivo) >= 0 and int(numeroEnlacesProducto) >= 0:

                    potencialPocp = calcularPocp(claseCov, region, pesoMolecular, constantekOh, numeroEnlaces, numeroCarbonos, constantekOhProductoNoReactivo,
                                                 rendimientoProductoNoReactivo, numeroEnlacesProducto, claseCovP, covsConOzono, covsAromatico, rendimientoCompuestoConOh)
                    print(potencialPocp)
                    covs.compuesto = compuesto
                    covs.formula = formula
                    covs.pesoMolecular = pesoMolecular
                    covs.constantekOh = constantekOh
                    covs.numeroEnlaces = numeroEnlaces
                    covs.numeroCarbonos = numeroCarbonos
                    covs.constantekOhProductoNoReactivo = constantekOhProductoNoReactivo
                    covs.claseCov = claseCov
                    covs.claseCovP = claseCovP
                    covs.rendimientoCompuestoConOh = rendimientoCompuestoConOh
                    covs.rendimientoProductoNoReactivo = rendimientoProductoNoReactivo
                    covs.numeroEnlacesProducto = numeroEnlacesProducto
                    covs.covsConOzono = covs.covsConOzono
                    covs.covsAromatico = covs.covsAromatico
                    covs.region = covs.region
                    covs.potencialPocp = potencialPocp
                    covs.save()
                    messages.success(
                        request, "Exito!! Ha editado el compuesto exitosamente")
                    return redirect('/')
                else:
                    messages.error(request, respuesta)
                    return render(request, 'ozono/editar.html')
            except:

                #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
                messages.error(request, respuesta)
                return render(request, 'ozono/editar.html')
        else:
            messages.error(request, respuesta)
            return render(request, 'ozono/editar.html', {'covs': covs})

    else:

        return render(request, 'ozono/editar.html', {'covs': covs})


def eliminarPocp(request, id):
    cov = Ozono.objects.get(id=id)
    cov.delete()
    listadoPotencialesPocp = Ozono.objects.all()
    return render(request, 'ozono/lista.html', {'listadoPotencialesPocp': listadoPotencialesPocp})


def displayPocp(request):
    listadoPotencialesPocp = Ozono.objects.all().values()
    df = pd.DataFrame(listadoPotencialesPocp)
    df2 = df['potencialPocp'].tolist()
    df3 = df['compuesto'].tolist()
    print(df3)
    print(df2)
    diccionario = {
        'df3': df3,
        'df2': df2,
        'ref': 'pocp'
    }
    return render(request, 'ozono/dashboard.html', context = diccionario)


def crearOdp(request):
    if request.method == 'POST':
        compuesto = str(request.POST['compuesto'])

        formula = str(request.POST['formula'])
        pesoMolecular = str(request.POST['pesoMolecular'])
        constantekOh = str(request.POST['constantekOh'])
        constantekCl = str(request.POST['constantekCl'])
        constantekO3 = str(request.POST['constantekO3'])
        constantekNo3 = str(request.POST['constantekNo3'])
        numeroCloro = str(request.POST['numeroCloro'])
        numeroBromo = str(request.POST['numeroBromo'])

        respuesta = validaOdp(compuesto, formula, pesoMolecular, numeroCloro,
                              numeroBromo, constantekOh, constantekCl, constantekO3, constantekNo3)

        if respuesta == None:
            try:

                tiempoGlobal = calculoTiempo(float(constantekOh), float(
                    constantekCl), float(constantekO3), float(constantekNo3))
                print(tiempoGlobal)
                potencialOdp = (tiempoGlobal / 60) * (137.37 / float(pesoMolecular)
                                                      ) * ((int(numeroCloro) + 30 * int(numeroBromo))) / 3
                print(potencialOdp)
                Odp(compuesto=compuesto, formula=formula, pesoMolecular=pesoMolecular, constantekOh=constantekOh, constantekCl=constantekCl, constantekO3=constantekO3,
                    constantekNo3=constantekNo3, tiempoGlobal=tiempoGlobal, numeroCloro=numeroCloro, numeroBromo=numeroBromo, potencialOdp=potencialOdp).save()
                messages.success(
                    request, "Exito!! Ha registrado el compuesto exitosamente")
                return redirect('/')

            except:

                #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
                messages.error(request, respuesta)
                return render(request, 'depletiono3/crear.html')
        else:
            messages.error(request, "Error, existen datos erroneos")
            return render(request, 'depletiono3/crear.html')
    else:

        return render(request, 'depletiono3/crear.html')


def edicionOdp(request, id):
    covs = Odp.objects.get(id=id)
    return render(request, 'depletiono3/editar.html', {'covs': covs})


def editarOdp(request):
    id = int(request.POST['id'])
    covs = Odp.objects.get(id=id)
    if request.method == 'POST':
        compuesto = str(request.POST['compuesto'])

        formula = str(request.POST['formula'])
        pesoMolecular = str(request.POST['pesoMolecular'])
        constantekOh = str(request.POST['constantekOh'])
        constantekCl = str(request.POST['constantekCl'])
        constantekO3 = str(request.POST['constantekO3'])
        constantekNo3 = str(request.POST['constantekNo3'])
        numeroCloro = str(request.POST['numeroCloro'])
        numeroBromo = str(request.POST['numeroBromo'])

        respuesta = validaOdp(compuesto, formula, pesoMolecular, numeroCloro,
                              numeroBromo, constantekOh, constantekCl, constantekO3, constantekNo3)

        if respuesta == None:
            try:

                tiempoGlobal = calculoTiempo(float(constantekOh), float(
                    constantekCl), float(constantekO3), float(constantekNo3))
                print(tiempoGlobal)
                potencialOdp = (tiempoGlobal / 60) * (137.37 / float(pesoMolecular)
                                                      ) * ((int(numeroCloro) + 30 * int(numeroBromo))) / 3
                print(potencialOdp)
                covs.compuesto = compuesto
                covs.formula = formula
                covs.pesoMolecular = pesoMolecular
                covs.constantekOh = constantekOh
                covs.constantekCl = constantekCl
                covs.constantekO3 = constantekO3
                covs.constantekNo3 = constantekNo3
                covs.tiempoGlobal = tiempoGlobal
                covs.numeroCloro = numeroCloro
                covs.numeroBromo = numeroBromo
                covs.potencialOdp = potencialOdp
                covs.save()
                messages.success(
                    request, "Exito!! Ha editado el compuesto exitosamente")
                return redirect('/')

            except:

                #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
                messages.error(request, respuesta)
                return render(request, 'depletiono3/editar.html')
        else:
            messages.error(request, "Error, existen datos erroneos")
            return render(request, 'depletiono3/editar.html', {'covs': covs})
    else:

        return render(request, 'depletiono3/editar.html', {'covs': covs})


def eliminarOdp(request, id):
    cov = Odp.objects.get(id=id)
    cov.delete()
    listadoPotencialesOdp = Odp.objects.all()
    return render(request, 'depletiono3/lista.html', {'listadoPotencialesOdp': listadoPotencialesOdp})


def listaOdp(request):
    listadoPotencialesOdp = Odp.objects.all()

    return render(request, 'depletiono3/lista.html', {'listadoPotencialesOdp': listadoPotencialesOdp})

def displayOdp(request):
    listadoPotencialesOdp = Odp.objects.all().values()
    df = pd.DataFrame(listadoPotencialesOdp)
    df2 = df['potencialOdp'].tolist()
    df3 = df['compuesto'].tolist()
    print(df3)
    print(df2)
    diccionario = {
        'df3': df3,
        'df2': df2,
        'ref': 'pocp'
    }
    return render(request, 'depletiono3/dashboard.html', context = diccionario)

def crearGwp(request):
    if request.method == 'POST':
        archivo_gwp = request.FILES['csvfile']

        data = pd.read_csv(archivo_gwp)
        lista_abs = list(data['abs'])
        compuesto = str(request.POST['compuesto'])
        formula = str(request.POST['formula'])
        constantekOh = str(request.POST['constantekOh'])
        constantekCl = str(request.POST['constantekCl'])
        constantekO3 = str(request.POST['constantekO3'])
        constantekNo3 = str(request.POST['constantekNo3'])
        concentration = str(request.POST['concentration'])
        opticalPath = str(request.POST['opticalPath'])
        pesoMolecular = str(request.POST['pesoMolecular'])
        tiempoGlobalGwp = calculoTimegwp(float(constantekOh), float(
            constantekCl), float(constantekO3), float(constantekNo3))
        print('este es el tiempo global ', tiempoGlobalGwp)
        # Hacer un vector de la referencia de CO2
        respuesta = validaGwp(compuesto, formula, pesoMolecular, concentration,
                              opticalPath, constantekOh, constantekCl, constantekO3, constantekNo3)
        if respuesta == None:
            try:
                archivo = 'impactos_atmosfericos/referencia_co2.csv'
                with open(archivo) as csvfile:  # Leo el archivo tipo diccionario
                    diccionario_secciones = list(csv.DictReader(csvfile))
                columna_co2 = "f_105"
                lista_co2 = []
                for i in range(len(diccionario_secciones)):
                    lista_co2.append(diccionario_secciones[i][columna_co2])

                lista_sint = []
                for i in range(len(lista_abs)):
                    lista_sint.append(
                        (float(lista_abs[i]) / (float(concentration) * float(opticalPath))) * 2.303)

                lista_f_sint = []
                for i in range(len(lista_co2)):
                    lista_f_sint.append(
                        float(lista_co2[i]) * float(lista_sint[i]) * 1E15 * 2.303)

                funcion_tiempo = (
                    (2.962*(tiempoGlobalGwp ** 0.9312)) / (1+(2.994*(tiempoGlobalGwp ** 0.9302))))
                print('esta es la función tiempo ', funcion_tiempo)
                lista_nueva = []

                for i in range(2500):  # Solo se necesita hasta 2500 valores
                    lista_nueva.append(lista_f_sint[i])
                rf_ghg = float(sum(lista_nueva))
                print(rf_ghg)
                rf_corrected = rf_ghg * funcion_tiempo
                print('este es rf_corrected ', rf_corrected)
                print('este es el peso molecular ', pesoMolecular)
                listaDePotencialesGwp = calculoGwp(
                    float(pesoMolecular), float(tiempoGlobalGwp), float(rf_corrected))
                print(listaDePotencialesGwp)
                globalWarming20 = listaDePotencialesGwp[0]

                globalWarming100 = listaDePotencialesGwp[1]

                globalWarming500 = listaDePotencialesGwp[2]

                print('gwp20 ', globalWarming20, 'gwp100 ',
                      globalWarming100, 'gwp500 ', globalWarming500)
                Gwp(compuesto=compuesto, formula=formula, pesoMolecular=pesoMolecular, constantekOh=constantekOh, constantekCl=constantekCl, constantekO3=constantekO3, constantekNo3=constantekNo3,
                    tiempoGlobalGwp=tiempoGlobalGwp, opticalPath=opticalPath, concentration=concentration, globalWarming20=globalWarming20, globalWarming100=globalWarming100, globalWarming500=globalWarming500).save()

                messages.success(
                    request, "Exito!! Ha registrado el compuesto exitosamente")
                return redirect('/')
            except:
                messages.error(request, 'hay un error de calculo')
                return render(request, 'gwppotential/crear.html')
        else:
            messages.error(request, "Error, existen datos erroneos")
            return render(request, 'gwppotential/crear.html')

    else:

        return render(request, 'gwppotential/crear.html')


def listaGwp(request):
    listadoPotencialesGwp = Gwp.objects.all()

    return render(request, 'gwppotential/lista.html', {'listadoPotencialesGwp': listadoPotencialesGwp})


def edicionGwp(request, id):
    covs = Gwp.objects.get(id=id)
    return render(request, 'gwppotential/editar.html', {'covs': covs})


def editarGwp(request):
    id = int(request.POST['id'])
    covs = Odp.objects.get(id=id)
    if request.method == 'POST':
        archivo_gwp = request.FILES['csvfile']

        data = pd.read_csv(archivo_gwp)
        lista_abs = list(data['abs'])
        compuesto = str(request.POST['compuesto'])
        formula = str(request.POST['formula'])
        constantekOh = str(request.POST['constantekOh'])
        constantekCl = str(request.POST['constantekCl'])
        constantekO3 = str(request.POST['constantekO3'])
        constantekNo3 = str(request.POST['constantekNo3'])
        concentration = str(request.POST['concentration'])
        opticalPath = str(request.POST['opticalPath'])
        pesoMolecular = str(request.POST['pesoMolecular'])
        tiempoGlobalGwp = calculoTimegwp(float(constantekOh), float(
            constantekCl), float(constantekO3), float(constantekNo3))
        print('este es el tiempo global ', tiempoGlobalGwp)
        # Hacer un vector de la referencia de CO2
        respuesta = validaGwp(compuesto, formula, pesoMolecular, concentration,
                              opticalPath, constantekOh, constantekCl, constantekO3, constantekNo3)
        if respuesta == None:
            try:
                archivo = 'impactos_atmosfericos/referencia_co2.csv'
                with open(archivo) as csvfile:  # Leo el archivo tipo diccionario
                    diccionario_secciones = list(csv.DictReader(csvfile))
                columna_co2 = "f_105"
                lista_co2 = []
                for i in range(len(diccionario_secciones)):
                    lista_co2.append(diccionario_secciones[i][columna_co2])

                lista_sint = []
                for i in range(len(lista_abs)):
                    lista_sint.append(
                        (float(lista_abs[i]) / (float(concentration) * float(opticalPath))) * 2.303)

                lista_f_sint = []
                for i in range(len(lista_co2)):
                    lista_f_sint.append(
                        float(lista_co2[i]) * float(lista_sint[i]) * 1E15 * 2.303)

                funcion_tiempo = (
                    (2.962*(tiempoGlobalGwp ** 0.9312)) / (1+(2.994*(tiempoGlobalGwp ** 0.9302))))
                print('esta es la función tiempo ', funcion_tiempo)
                lista_nueva = []

                for i in range(2500):  # Solo se necesita hasta 2500 valores
                    lista_nueva.append(lista_f_sint[i])
                rf_ghg = float(sum(lista_nueva))
                print(rf_ghg)
                rf_corrected = rf_ghg * funcion_tiempo
                print('este es rf_corrected ', rf_corrected)
                print('este es el peso molecular ', pesoMolecular)
                listaDePotencialesGwp = calculoGwp(
                    float(pesoMolecular), float(tiempoGlobalGwp), float(rf_corrected))
                print(listaDePotencialesGwp)
                globalWarming20 = listaDePotencialesGwp[0]

                globalWarming100 = listaDePotencialesGwp[1]

                globalWarming500 = listaDePotencialesGwp[2]

                covs.compuesto = compuesto
                covs.formula = formula
                covs.pesoMolecular = pesoMolecular
                covs.constantekOh = constantekOh
                covs.constantekCl = constantekCl
                covs.constantekO3 = constantekO3
                covs.constantekNo3 = constantekNo3
                covs.tiempoGlobalGwp = tiempoGlobalGwp
                covs.opticalPath = opticalPath
                covs.concentration = concentration
                covs.globalWarming20 = globalWarming20
                covs.globalWarming100 = globalWarming100
                covs.globalWarming500 = globalWarming500
                covs.save()
                messages.success(
                    request, "Exito!! Ha registrado el compuesto exitosamente")
                return redirect('/')
            except:
                messages.error(request, 'hay un error de calculo')
                return render(request, 'gwppotential/editar.html')
        else:
            messages.error(request, "Error, existen datos erroneos")
            return render(request, 'gwppotential/editar.html')
    else:
        return render(request, 'gwppotential/editar.html')


def eliminarGwp(request, id):
    cov = Gwp.objects.get(id=id)
    cov.delete()
    listadoPotencialesGwp = Gwp.objects.all()
    return render(request, 'gwppotential/lista.html', {'listadoPotencialesGwp': listadoPotencialesGwp})


def crearTiempo(request):
    if request.method == 'POST':
        compuesto = str(request.POST['compuesto'])
        formula = str(request.POST['formula'])
        constantekOh = str(request.POST['constantekOh'])
        constantekCl = str(request.POST['constantekCl'])
        constantekO3 = str(request.POST['constantekO3'])
        constantekNo3 = str(request.POST['constantekNo3'])

        respuesta = validaTiempo(
            compuesto, formula, constantekOh, constantekCl, constantekO3, constantekNo3)

        try:
            if respuesta == None:

                listaDeTiempos = listaTiempo(float(constantekOh), float(
                    constantekCl), float(constantekO3), float(constantekNo3))
                tiempoOh = listaDeTiempos[0]
                tiempoCl = listaDeTiempos[1]
                tiempoO3 = listaDeTiempos[2]
                tiempoNo3 = listaDeTiempos[3]
                Tiempo(compuesto=compuesto, formula=formula, tiempoOh=tiempoOh,
                       tiempoCl=tiempoCl, tiempoO3=tiempoO3, tiempoNo3=tiempoNo3).save()

                messages.success(
                    request, "Exito!! Ha registrado el compuesto exitosamente")
                return redirect('/')
            else:
                messages.error(request, "Error, existen datos vacios")
                return render(request, 'timeTropospheric/crear.html')

        except:

            #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
            messages.error(request, respuesta)
            return render(request, 'timeTropospheric/crear.html')

    else:

        return render(request, 'timeTropospheric/crear.html')


def listaTime(request):
    listadoDeTiempos = Tiempo.objects.all()

    return render(request, 'timeTropospheric/lista.html', {'listadoDeTiempos': listadoDeTiempos})


def edicionTime(request, id):
    covs = Tiempo.objects.get(id=id)
    return render(request, 'timeTropospheric/editar.html', {'covs': covs})


def editarTime(request):
    id = int(request.POST['id'])
    covs = Tiempo.objects.get(id=id)
    if request.method == 'POST':
        compuesto = str(request.POST['compuesto'])
        formula = str(request.POST['formula'])
        constantekOh = str(request.POST['constantekOh'])
        constantekCl = str(request.POST['constantekCl'])
        constantekO3 = str(request.POST['constantekO3'])
        constantekNo3 = str(request.POST['constantekNo3'])

        respuesta = validaTiempo(compuesto, formula, constantekOh, constantekCl, constantekO3, constantekNo3)

        try:
            if respuesta == None:

                listaDeTiempos = listaTiempo(float(constantekOh), float(constantekCl), float(constantekO3), float(constantekNo3))
                tiempoOh = listaDeTiempos[0]
                tiempoCl = listaDeTiempos[1]
                tiempoO3 = listaDeTiempos[2]
                tiempoNo3 = listaDeTiempos[3]

                covs.compuesto = compuesto
                covs.formula = formula
                covs.tiempoOh = tiempoOh
                covs.tiempoCl = tiempoCl
                covs.tiempoO3 = tiempoO3
                covs.tiempoNo3 = tiempoNo3
                covs.save()
                messages.success(request, "Exito!! Ha editado el compuesto exitosamente")
                return redirect('/')
            else:
                messages.error(request, "Error, existen datos vacios")
                return render(request, 'timeTropospheric/editar.html')

        except:

            #respuesta = valida(compuesto, formula, pesoMolecular, fluor, cloro, nitrogeno, azufre)
            messages.error(request, respuesta)
            return render(request, 'timeTropospheric/editar.html')

    else:

        return render(request, 'timeTropospheric/editar.html')


def eliminarTime(request, id):
    cov = Tiempo.objects.get(id=id)
    cov.delete()
    listadoDeTiempos = Tiempo.objects.all()
    return render(request, 'timeTropospheric/lista.html', {'listadoDeTiempos': listadoDeTiempos})