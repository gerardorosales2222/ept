# Generated by Django 5.0.6 on 2024-06-18 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_obrero_obreros_alter_material_de_epp_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epp',
            name='nombre_epp',
            field=models.CharField(max_length=40, null=True, verbose_name='marca'),
        ),
    ]
