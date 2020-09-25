from django.db import models

class Flor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    descripcion = models.TextField(blank = False, null = False)
    precio = models.DecimalField(max_digits = 6, decimal_places = 2)


    class Meta:
        verbose_name = 'Flor'
        verbose_name_plural = 'Flores' 
        ordering = ['nombre']

    def __str__(self):
        return self.nombre