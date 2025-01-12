# Este es tu archivo de URLs de la aplicación (por ejemplo, en la carpeta de la aplicación de 'core')
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .models import CustomAuthToken
from .views import CompañíaViewSet, ProyectoViewSet, HistoriaDeUsuarioViewSet, EstadoViewSet, TicketViewSet, UsuarioViewSet

# Crear el router para la API
router = DefaultRouter()
router.register(r'compañias', CompañíaViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'historias', HistoriaDeUsuarioViewSet)
router.register(r'estados', EstadoViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'usuarios', UsuarioViewSet)
urlpatterns = [
    path('api/', include(router.urls)),  # Rutas de la API
    path('custom-token-auth/', CustomAuthToken.as_view(), name='custom_token_auth'),
]
