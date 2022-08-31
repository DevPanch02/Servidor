from turtle import mode
from django.db import models

class Page(models.Model):
    start=models.CharField(default='Inicio', max_length=30)
    importar=models.CharField(default='Importar', max_length=30)
    list=models.CharField(default='Listar', max_length=30)
    person=models.CharField(default='Personal', max_length=30)

    def __str__(self) :
        return f" {self.start}, {self.importar}, {self.list}, {self.person} "

    