from django import forms 

from .models import Categoria, SubCategoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields = ['description','estado']
        labels = {'description':" Descripcion de la Categoria",
                  "estado":"Estado"}
        widget={'description': forms.TextInput}

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in iter(self.fields):
        self.fields[field].widget.attrs.update({
            'class':'form-control'
        })



class SubCategoriaForm(forms.ModelForm):
    class Meta:
        model=SubCategoria
        fields = ['categoria','description','estado']
        labels = {'description':" Sub Categoria",
                  "estado":"Estado"}
        widget={'description': forms.TextInput}

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in iter(self.fields):
        self.fields[field].widget.attrs.update({
            'class':'form-control'
        })
    self.fields['categoria'].empty_label = "Seleccione Categoria"



        