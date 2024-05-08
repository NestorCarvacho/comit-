from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('index', index, name="index"),
    path('login/', user_login, name='login'),
    path('administrar-cuota-persona/', administracionCuotaPersona, name='administrar-cuota-persona'),
    path('administrar-cuota-persona/crear-cuota-persona', crearCuotaPersona, name='crear-cuota-persona'),
    path('administrar-cuota-persona/modificar-cuota-persona/<int:id_cuota_persona>', editarCuotaPersona, name='modificar-cuota-persona'),
    path('administrar-cuota-persona/eliminar-cuota-persona/<int:id_cuota_persona>', eliminarCuotaPersona, name='eliminar-cuota-persona'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)