from django.db import models

from bases.models import ClaseModelo  

class Categoria(ClaseModelo):  
    description = models.CharField(  
        max_length=100,
        help_text='Descripcion de la Categoria',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.description)

    def save(self, *args, **kwargs): 
        self.description = self.description.upper()
        super(Categoria, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categorias"  
