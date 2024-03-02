from django.db import models

class Language(models.Model):
    nombre = models.CharField(max_length=10)
    creador = models.CharField(max_length=15)
    version = models.IntegerField()
    descripcion = models.TextField()
    
    def __str__(self):
        return f"{self.nombre}"

class Framework(models.Model):
    nombre = models.CharField(max_length=10)
    languages = models.CharField(max_length=15)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre}"