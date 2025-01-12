from django.urls import include, path
from . import views
from .forms import CompaniaViewSet, ProyectoViewSet, HistoriaDeUsuarioViewSet, EstadoViewSet, TicketViewSet, UsuarioViewSet
from rest_framework.routers import DefaultRouter
from .forms import CompaniaViewSet, ProyectoViewSet, HistoriaDeUsuarioViewSet, EstadoViewSet, TicketViewSet, UsuarioViewSet

# Rutas de la API
router = DefaultRouter()
router.register(r'companias', CompaniaViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'historias', HistoriaDeUsuarioViewSet)
router.register(r'estados', EstadoViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', views.CustomAuthToken.as_view(), name='custom-auth-token'),
    path('login/', views.login_view, name='login'),
     path('api/register/', views.crear_usuario, name='crear_usuario'),
    path('crear_historia/', views.crear_historia, name='crear_historia'),
    path('crear_ticket/', views.crear_ticket, name='crear_ticket'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
]
