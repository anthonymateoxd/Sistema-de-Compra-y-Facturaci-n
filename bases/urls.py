from django.urls import path

from bases.views import Home  # Asegúrate de que esta importación sea correcta

urlpatterns = [
    path('',include(('bases.urls','bases'), namespace='bases')),
    path('admin/', admin.site.urls)
]