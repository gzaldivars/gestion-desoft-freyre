# Generated by Django 4.1.2 on 2022-11-15 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('alias', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=8)),
                ('reeup', models.CharField(max_length=15)),
                ('nit', models.CharField(max_length=15)),
                ('cuenta_bancaria', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='ContratoMarco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_contrato', models.CharField(max_length=15)),
                ('fecha_firma', models.DateField(null=True)),
                ('estado_contrato', models.CharField(choices=[('OP', 'OPORTUNIDAD'), ('SOL', 'SOLICITADO'), ('REC', 'RECIBIDO'), ('FIR', 'FIRMADO'), ('CLO', 'CERRADO'), ('CAN', 'CANCELADO')], default='OP', max_length=15)),
                ('nivel_contratacion', models.CharField(choices=[('MUN', 'MUNICIPIO'), ('PRV', 'PROVINCIA'), ('OTR', 'OTRO')], default='MUN', max_length=10)),
            ],
            options={
                'verbose_name': 'contrato marco',
                'verbose_name_plural': 'contratos marco',
            },
        ),
        migrations.CreateModel(
            name='DetallesFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('importe', models.FloatField()),
                ('fecha_facturacion', models.DateField(null=True)),
                ('estado', models.CharField(choices=[('FIR', 'FIRMADA'), ('CAN', 'CANCELADA'), ('LIQ', 'LIQUIDADA')], max_length=15)),
            ],
            options={
                'verbose_name': 'factura',
                'verbose_name_plural': 'facturas',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.DateField()),
                ('year', models.DateField()),
                ('importe', models.FloatField()),
                ('confirmado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'planes',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'producto o servicio',
                'verbose_name_plural': 'productos o servicios',
            },
        ),
        migrations.CreateModel(
            name='Surtido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'surtido',
                'verbose_name_plural': 'surtidos',
            },
        ),
        migrations.CreateModel(
            name='ContratoEspecifico',
            fields=[
                ('contratomarco_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cmi_brigada.contratomarco')),
                ('numero', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name': 'contrato especifico',
                'verbose_name_plural': 'contratos especificos',
            },
            bases=('cmi_brigada.contratomarco',),
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmi_brigada.plan')),
            ],
        ),
    ]
