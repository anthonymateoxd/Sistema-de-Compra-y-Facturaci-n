from django import forms 

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto


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
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('description')
    )
    class Meta:
        model=SubCategoria
        fields = ['categoria','description','estado']
        labels = {'description':"Sub Categoria",
               "estado":"Estado"}
        widget={'description': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['categoria'].empty_label =  "Seleccione Categoria"

class MarcaForm(forms.ModelForm):
    class Meta:
        model=Marca
        fields = ['description','estado']
        labels= {'description': "Descripcion de la Marca",
                "estado":"Estado"}
        widget={'description': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UMForm(forms.ModelForm):
    class Meta:
        model=UnidadMedida
        fields = ['description','estado']
        labels= {'description': "Descripcion de la Marca",
                "estado":"Estado"}
        widget={'description': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['codigo','codigo_barra','description','estado', \
                'precio','existencia','ultima_compra',
                'marca','subcategoria','unidad_medida']
        exclude = ['um','fm','uc','fc']
        widget={'description': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True       