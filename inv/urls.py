from django.urls import include, path 

from .views import CategoriaView, CategoriaNew


urlpatterns = [
    path('categorias/',CategoriaView.as_view(), name='categoria_list'),

]   