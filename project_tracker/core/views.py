from rest_framework import viewsets
from .models import Compañía, Proyecto, HistoriaDeUsuario, Estado, Ticket, Usuario
from .serializers import CompañíaSerializer, ProyectoSerializer, HistoriaDeUsuarioSerializer, EstadoSerializer, TicketSerializer, UsuarioSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .serializers import LoginSerializer

# Vista para Compañía
class CompañíaViewSet(viewsets.ModelViewSet):
    queryset = Compañía.objects.all()
    serializer_class = CompañíaSerializer

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
