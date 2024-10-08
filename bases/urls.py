from django.urls import path
from .views import SomeView  # Importa la vista que necesitas

urlpatterns = [
     path('', SomeView.as_view(), name='some_view'),
    path('',include(('bases.urls','bases'), namespace='bases')),
    path('admin/', admin.site.urls)
]