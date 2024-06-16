# Generated by Django 5.0.6 on 2024-06-13 03:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='material_de_epp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_material', models.CharField(max_length=20, verbose_name='Nombre Material')),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'Materiales',
                'db_table': 'material',
            },
        ),
        migrations.CreateModel(
            name='obrero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legajo', models.CharField(max_length=4, verbose_name='Legajo')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='Apellido')),
                ('tel', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('género', models.CharField(choices=[('V', 'Varón'), ('M', 'Mujer')], max_length=1)),
            ],
            options={
                'verbose_name': 'obrero',
                'verbose_name_plural': 'Obreros',
                'db_table': 'obrero',
            },
        ),
        migrations.CreateModel(
            name='supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legajo', models.CharField(max_length=4, verbose_name='Legajo')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='Apellido')),
                ('tel', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('género', models.CharField(choices=[('V', 'Varón'), ('M', 'Mujer')], max_length=1)),
            ],
            options={
                'verbose_name': 'supervisor',
                'verbose_name_plural': 'Supervisores',
                'db_table': 'supervisor',
            },
        ),
        migrations.CreateModel(
            name='tipo_cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cargo', models.CharField(max_length=20, verbose_name='Nombre_Cargo')),
                ('descripción', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'tipo_cargo',
                'verbose_name_plural': 'Tipos de Cargos',
                'db_table': 'tipo_cargo',
            },
        ),
        migrations.CreateModel(
            name='epp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_epp', models.CharField(max_length=20, verbose_name='nombre_EPP')),
                ('stock', models.PositiveIntegerField(default=100)),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.material_de_epp')),
            ],
            options={
                'verbose_name': 'EPP',
                'verbose_name_plural': 'Elementos de Protección Personal',
                'db_table': 'EPP',
            },
        ),
        migrations.CreateModel(
            name='orden_de_retiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField()),
                ('retirado', models.BooleanField(default=False)),
                ('epp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.epp')),
                ('obrero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.obrero')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.supervisor')),
            ],
            options={
                'verbose_name': 'orden de retiro',
                'verbose_name_plural': 'Ordenes de Retiro',
                'db_table': 'orden de retiro',
            },
        ),
        migrations.AddField(
            model_name='obrero',
            name='cargo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.tipo_cargo'),
        ),
    ]