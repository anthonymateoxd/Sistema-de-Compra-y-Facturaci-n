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

class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    description = models.CharField(  
        max_length=100,
        help_text='Descripcion de la Categoria',
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.description,self.description)
    
    def save(self, *args, **kwargs): 
        self.description = self.description.upper()
        super(SubCategoria, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = " Sub Categorias"  
        unique_together = ('categoria', 'description')


                                       
