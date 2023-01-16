from django.db import models

# Create your models here.

class Acidificacion(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    compuesto = models.CharField(
        max_length=150, verbose_name="compuesto", null=True)
    formula = models.CharField(
        max_length=150, verbose_name="formula", null=True)
    pesoMolecular = models.FloatField(verbose_name="pesoMolecular", null=True)
    fluor = models.PositiveIntegerField(verbose_name="fluor", null=True)
    cloro = models.PositiveIntegerField(verbose_name="cloro", null=True)
    nitrogeno = models.PositiveIntegerField(
        verbose_name="nitrogeno", null=True)
    azufre = models.PositiveIntegerField(verbose_name="azufre", null=True)
    potencialap = models.FloatField(verbose_name="potencialap", null=True)

    def __str__(self):
        
        return self.compuesto

class Tiempo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    compuesto = models.CharField(max_length=150, verbose_name="compuesto", null=True)
    formula = models.CharField(max_length=150, verbose_name="formula", null=True)
    tiempoOh = models.FloatField(verbose_name="tiempoOh", null=True)
    tiempoCl = models.FloatField(verbose_name="tiempoCl", null=True)
    tiempoO3 = models.FloatField(verbose_name="tiempoO3", null=True)
    tiempoNo3 = models.FloatField(verbose_name="tiempoNo3", null=True)

    def __str__(self):
        
        return self.compuesto

class Ozono(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    compuesto = models.CharField(
        max_length=150, verbose_name="compuesto", null=True)
    formula = models.CharField(
        max_length=150, verbose_name="formula", null=True)
    pesoMolecular = models.FloatField(verbose_name="pesoMolecular", null=True)
    constantekOh = models.FloatField(verbose_name="constantekOh", null=True)
    constantekO3 = models.FloatField(verbose_name="constantekO3", null=True)
    rendimientoCompuestoConOh = models.FloatField(verbose_name="rendimientoCompuestoConOh", null=True)
    claseCov = models.CharField(
        max_length=150, verbose_name="claseCov", null=True)
    region = models.CharField(
        max_length=150, verbose_name="region", null=True)
    numeroEnlaces = models.PositiveIntegerField(verbose_name="numeroEnlaces", null=True)
    numeroCarbonos = models.PositiveIntegerField(verbose_name="numeroCarbonos", null=True)
    constantekOhProductoNoReactivo = models.FloatField(verbose_name="constantekOhProductoNoReactivo", null=True)
    rendimientoProductoNoReactivo = models.FloatField(verbose_name="rendimientoProductoNoReactivo", null=True)
    numeroEnlacesProducto = models.PositiveIntegerField(verbose_name="numeroEnlacesProducto", null=True)
    claseCovP = models.CharField(
        max_length=150, verbose_name="claseCovP", null=True)
    covsConOzono = models.CharField(
        max_length=150, verbose_name="covsConOzono", null=True)
    covsAromatico = models.CharField(
        max_length=150, verbose_name="covsAromatico", null=True)
    potencialPocp = models.FloatField(verbose_name="potencialPocp", null=True)

    def __str__(self):
        
        return self.compuesto


class Odp(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    compuesto = models.CharField(max_length=150, verbose_name="compuesto", null=True)
    formula = models.CharField(max_length=150, verbose_name="formula", null=True)
    pesoMolecular = models.FloatField(verbose_name="pesoMolecular", null=True)
    constantekOh = models.FloatField(verbose_name="constantekOh", null=True)
    constantekCl = models.FloatField(verbose_name="constantekCl", null=True)
    constantekO3 = models.FloatField(verbose_name="constantekO3", null=True)
    constantekNo3 = models.FloatField(verbose_name="constantekNo3", null=True)
    tiempoGlobal = models.FloatField(verbose_name="tiempoGlobal", null=True)
    numeroCloro = models.IntegerField(verbose_name="numeroCloro",null=True)
    numeroBromo = models.IntegerField(verbose_name="numeroBromo", null=True)
    potencialOdp = models.FloatField(verbose_name="potencialOdp", null=True)

    def __str__(self):
        
        return self.compuesto

class File(models.Model):
    file = models.FileField(upload_to="files")

class Gwp(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    compuesto = models.CharField(max_length=150, verbose_name="compuesto", null=True)
    formula = models.CharField(max_length=150, verbose_name="formula", null=True)
    pesoMolecular = models.FloatField(verbose_name="pesoMolecular", null=True)
    constantekOh = models.FloatField(verbose_name="constantekOh", null=True)
    constantekCl = models.FloatField(verbose_name="constantekCl", null=True)
    constantekO3 = models.FloatField(verbose_name="constantekO3", null=True)
    constantekNo3 = models.FloatField(verbose_name="constantekNo3", null=True)
    tiempoGlobalGwp = models.FloatField(verbose_name="tiempoGlobalGwp", null=True)
    opticalPath = models.FloatField(verbose_name="=opticalPath",null=True)
    concentration = models.FloatField(verbose_name="concentration",null=True)
    globalWarming20 = models.FloatField(verbose_name="globalWarming20", null=True)
    globalWarming100 = models.FloatField(verbose_name="globalWarming100", null=True)
    globalWarming500 = models.FloatField(verbose_name="globalWarming500", null=True)

    def __str__(self):
        
        return self.compuesto
