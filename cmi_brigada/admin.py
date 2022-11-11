from django.contrib import admin
from cmi_brigada.models import Cliente, ContratoMarco, ContratoEspecifico, Factura, DetallesFactura, Surtido, ProductoServicio

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion',)
    search_fields = ('nombre', 'direccion',)
    list_filter = ('nombre', 'direccion',)


admin.site.register(Cliente)
#admin.site.register(ContratoAbstracto)
admin.site.register(ContratoMarco)
admin.site.register(ContratoEspecifico)
admin.site.register(Factura)
admin.site.register(DetallesFactura)
admin.site.register(Surtido)
admin.site.register(ProductoServicio)