from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=70)
    alias = models.CharField(max_length=20)
    especialista = User.username
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

class ContratoMarco(models.Model):
    cod_contrato = models.CharField(max_length=15)
    fecha_firma =  models.DateField(null=True)
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
    
    class Meta:
        verbose_name = 'contrato marco'
        verbose_name_plural = 'contratos marco'
    
    def __str__(self):
        return self.cod_contrato

class ContratoEspecifico(ContratoMarco):
    numero = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'contrato especifico'
        verbose_name_plural = 'contratos especificos'
    
    def __str__(self):
        return super(self.cod_contrato) + self.numero

class Surtido(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'surtido'
        verbose_name_plural = 'surtidos'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    "Esta clase es utilizada para definir los productos y los servicios"
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'producto o servicio'
        verbose_name_plural = 'productos o servicios'

    def __str__(self):
        return self.nombre + self.descripcion

class Factura(models.Model):
    codigo = models.CharField(max_length=20)
    #contrato
    importe = models.FloatField()
    fecha_facturacion = models.DateField(null=True)

    ESTADO_FACTURA_CHOICES = [
        ('FIR', 'FIRMADA'),
        ('CAN', 'CANCELADA'),
        ('LIQ','LIQUIDADA')
    ]
    estado = models.CharField(max_length=15, choices=ESTADO_FACTURA_CHOICES)
    #produccion_mes

    class Meta:
        verbose_name = 'factura'
        verbose_name_plural = 'facturas'

    def __str__(self):
        return self.codigo

class DetallesFactura(models.Model):
    pass

class Plan(models.Model):
    mes = models.DateField()
    year = models.DateField()
    importe = models.FloatField()
    confirmado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'plan'
        verbose_name = 'planes'

class Produccion(models.Model):
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)
    especialista = User.get_username
