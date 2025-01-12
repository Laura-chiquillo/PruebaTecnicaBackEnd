from rest_framework import viewsets
from .models import Compania, Proyecto, HistoriaDeUsuario, Estado, Ticket, Usuario
from .serializers import CompaniaSerializer, ProyectoSerializer, HistoriaDeUsuarioSerializer, EstadoSerializer, TicketSerializer, UsuarioSerializer


# Vista para Compañía
class CompaniaViewSet(viewsets.ModelViewSet):
    queryset = Compania.objects.all()
    serializer_class = CompaniaSerializer

# Vista para Proyecto
class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

# Vista para Historia de Usuario
class HistoriaDeUsuarioViewSet(viewsets.ModelViewSet):
    queryset = HistoriaDeUsuario.objects.all()
    serializer_class = HistoriaDeUsuarioSerializer

# Vista para Estado
class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

# Vista para Ticket
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

# Vista para Usuario
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
