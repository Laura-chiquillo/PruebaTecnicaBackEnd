from rest_framework import serializers
from .models import Compañía, Proyecto, HistoriaDeUsuario, Estado, Ticket, Usuario
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    contrasena = serializers.CharField(write_only=True)

# Serializador para la Compañía
class CompañíaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compañía
        fields = '__all__'

# Serializador para Proyecto
class ProyectoSerializer(serializers.ModelSerializer):
    compañía = CompañíaSerializer()
    
    class Meta:
        model = Proyecto
        fields = '__all__'

# Serializador para Historia de Usuario
class HistoriaDeUsuarioSerializer(serializers.ModelSerializer):
    proyecto = ProyectoSerializer()
    
    class Meta:
        model = HistoriaDeUsuario
        fields = '__all__'

# Serializador para Estado
class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

# Serializador para Ticket
class TicketSerializer(serializers.ModelSerializer):
    historia_de_usuario = HistoriaDeUsuarioSerializer()
    estado = EstadoSerializer()
    
    class Meta:
        model = Ticket
        fields = '__all__'

# Serializador para Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()  # Mostrar el nombre de usuario asociado
    
    class Meta:
        model = Usuario
        fields = '__all__'
