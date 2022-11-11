from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=70)
    alias = models.CharField(max_length=20)
    #especialista = models.ForeignKey()
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=8)
    reeup = models.CharField(max_length=15)
    nit = models.CharField(max_length=15)
    cuenta_bancaria = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
    
    def __str__(self):
        return self.nombre 

class ContratoAbstracto(models.Model):
    fecha_firma =  models.DateField()
    ESTADO_CONTRATO_CHOICES = [
        ('OP', 'OPORTUNIDAD'),
        ('SOL', 'SOLICITADO'),
        ('REC', 'RECIBIDO'),
        ('FIR', 'FIRMADO'),
        ('CLO', 'CERRADO'),
        ('CAN', 'CANCELADO'),
    ]
    estado_contrato = models.CharField(max_length=15, choices=ESTADO_CONTRATO_CHOICES, default='OP')
    LUGAR_FIRMA_CHOICES = [
        ('MUN', 'MUNICIPIO'),
        ('PRV', 'PROVINCIA'),
        ('OTR', 'OTRO')
    ]
    nivel_contratacion = models.CharField(max_length=10, choices=LUGAR_FIRMA_CHOICES, default='MUN')

class ContratoMarco(ContratoAbstracto):
    cod_contrato = models.CharField(max_length=15)
    #cliente = models.CharField(max_length=15)
    #fecha = models.DateField()    
    
    class Meta:
        verbose_name = 'contrato marco'
        verbose_name_plural = 'contratos marco'
    
    def __str__(self):
        return self.cod_contrato

class ContratoEspecifico(ContratoAbstracto):
    #marco = models.ForeignKey(ContratoMarco)
    numero = models.CharField(max_length=5)

class Surtido(models.Model):
    pass

class ProductoServicio(models.Model):
    pass

class Factura(models.Model):
    pass

class DetallesFactura(models.Model):
    pass

