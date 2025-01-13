from rest_framework import viewsets
from .models import Compania, Proyecto, HistoriaDeUsuario, Estado, Ticket, Usuario
from .serializers import CompaniaSerializer, ProyectoSerializer, HistoriaDeUsuarioSerializer, EstadoSerializer, TicketSerializer, UsuarioSerializer

class CompaniaViewSet(viewsets.ModelViewSet):
    queryset = Compania.objects.all()
    serializer_class = CompaniaSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class HistoriaDeUsuarioViewSet(viewsets.ModelViewSet):
    queryset = HistoriaDeUsuario.objects.all()
    serializer_class = HistoriaDeUsuarioSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
