from django.db import models

class Productor(models.Model):
    documento = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

class Finca(models.Model):
    numero_catastro = models.CharField(max_length=50)
    municipio = models.CharField(max_length=100)
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE, related_name='fincas')

class Vivero(models.Model):
    codigo = models.CharField(max_length=50)
    tipo_cultivo = models.CharField(max_length=100)
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, related_name='viveros')

class Labor(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField()
    vivero = models.ForeignKey(Vivero, on_delete=models.CASCADE, related_name='labores')
    productos = models.ManyToManyField('ControlPlagas', through='LaborProductoControl')


class ProductoControl(models.Model):
    registro_ICA = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    frecuencia_aplicacion = models.IntegerField()
    valor = models.FloatField()
    class Meta:
        abstract = True

class ControlPlagas(ProductoControl):
    periodo_carencia = models.IntegerField()

class ControlFertilizantes(ProductoControl):
    fecha_ultima_aplicacion = models.DateField()

class ControlHongos(ProductoControl):
    periodo_carencia = models.IntegerField()
    nombre_hongo = models.CharField(max_length=100)

class LaborProductoControl(models.Model):
    labor = models.ForeignKey(Labor, on_delete=models.CASCADE)
    producto = models.ForeignKey(ControlPlagas, on_delete=models.CASCADE)

# Registrar modelos en el admin de Django
from django.contrib import admin
admin.site.register(Productor)
admin.site.register(Finca)
admin.site.register(Vivero)
admin.site.register(Labor)
admin.site.register(ControlPlagas)
admin.site.register(ControlFertilizantes)
admin.site.register(ControlHongos)
admin.site.register(LaborProductoControl)

