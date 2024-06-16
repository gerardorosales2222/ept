from django.db import models

class tipo_cargo(models.Model):
    nombre_cargo = models.CharField(max_length=20, null=False, verbose_name='Nombre_Cargo')
    descripción = models.CharField(max_length=100, null=False, verbose_name='Descripción')
    def __str__(self):
        return '%s'%(self.nombre_cargo)
    class Meta:
        db_table = 'tipo_cargo'
        verbose_name = 'tipo_cargo'
        verbose_name_plural = 'Tipos de Cargos'

class obrero(models.Model):
    legajo = models.CharField(max_length=4, null=False, verbose_name='Legajo')
    cargo = models.ForeignKey(tipo_cargo, on_delete=models.CASCADE, blank=True, null=True)
    dni = models.CharField(max_length=8, null=False, verbose_name='DNI')
    nombre = models.CharField(max_length=20, null=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, null=False, verbose_name='Apellido')
    tel = models.CharField(max_length=10, null=False, verbose_name='Teléfono')
    géneros = [('V', 'Varón'),('M', 'Mujer'),]
    género = models.CharField(max_length=1, choices=géneros)
    def __str__(self):
        return '%s %s  %s'%(self.legajo, self.apellido, self.nombre)  
    class Meta:
        db_table = 'obrero'
        verbose_name = 'obrero'
        verbose_name_plural = 'Obreros'
        
class tipo_supervisor(models.Model):
    titulo = models.CharField(max_length=30, null=False, verbose_name='Título')
    descripción = models.CharField(max_length=30, null=False, verbose_name='Descripción')
    def __str__(self):
        return '%s'%(self.titulo)  
    class Meta:
        db_table = 'tipo_supervisor'
        verbose_name = 'Tipo de Supervisor'
        verbose_name_plural = 'Tipos de Supervisores'
        
class supervisor(models.Model):
    legajo = models.CharField(max_length=4, null=False, verbose_name='Legajo')
    dni = models.CharField(max_length=8, null=False, verbose_name='DNI')
    nombre = models.CharField(max_length=20, null=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, null=False, verbose_name='Apellido')
    cargo = models.ForeignKey(tipo_supervisor, on_delete=models.CASCADE, blank=True, null=True)
    tel = models.CharField(max_length=10, null=False, verbose_name='Teléfono')
    géneros = [('V', 'Varón'),('M', 'Mujer'),]
    género = models.CharField(max_length=1, choices=géneros)
    def __str__(self):
        return '%s  %s'%(self.nombre, self.apellido)  
    class Meta:
        db_table = 'supervisor'
        verbose_name = 'supervisor'
        verbose_name_plural = 'Supervisores'
        
class material_de_epp(models.Model):
    nombre_material = models.CharField(max_length=50, null=False, verbose_name='Nombre Material')
    def __str__(self):
        return '%s '%(self.nombre_material)  
    class Meta:
        db_table = 'material'
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'
        
class epp(models.Model):
    nombre_epp = models.CharField(max_length=20, null=False, verbose_name='nombre_EPP')
    material = models.ForeignKey(material_de_epp, on_delete=models.CASCADE, blank=True, null=True)
    stock = models.PositiveIntegerField(default=100)
    def __str__(self):
        return '%s  %s'%(self.nombre_epp, self.material)  
    class Meta:
        db_table = 'EPP'
        verbose_name = 'EPP'
        verbose_name_plural = 'Elementos de Protección Personal'
        
class orden_de_retiro(models.Model):
    codigo = models.PositiveIntegerField()
    obrero = models.ForeignKey(obrero, on_delete=models.CASCADE, blank=True, null=True)
    epp =models.ForeignKey(epp, on_delete=models.CASCADE, blank=True, null=True)
    supervisor = models.ForeignKey(supervisor, on_delete=models.CASCADE, blank=True, null=True)
    retirado = models.BooleanField(default=False)
    def __str__(self):
        return '%s  %s'%(self.codigo, self.epp)  
    class Meta:
        db_table = 'orden de retiro'
        verbose_name = 'orden de retiro'
        verbose_name_plural = 'Ordenes de Retiro'