from django.db import models
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

# Modelo para la Compañía
class Compania(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    correo = models.EmailField()

    class Meta:
        db_table = 'compania'

# Modelo para Proyecto
class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    Compania = models.ForeignKey(Compania, related_name='proyectos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        db_table = 'proyecto'

# Modelo para Historia de Usuario
class HistoriaDeUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    proyecto = models.ForeignKey(Proyecto, related_name='historias', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    class Meta:
        db_table = 'historiaDeUsuario'

# Modelo para Estado del Ticket
class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'estado'

# Modelo para Ticket de Desarrollo
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    historiaDeUsuario = models.ForeignKey(HistoriaDeUsuario, related_name='tickets', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    comentarios = models.TextField(blank=True)
    estado = models.ForeignKey(Estado, related_name='tickets', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'ticket'

# Modelo para Usuario
class Usuario(models.Model):
    cedula = models.CharField(max_length=50, primary_key=True)
    contrasena = models.CharField(max_length=128)
    correo = models.CharField(max_length=150)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Compania = models.ManyToManyField(Compania, related_name='usuarios', blank=True)

    class Meta:
        db_table = 'usuario'


class CustomAuthToken(APIView):
    def post(self, request, *args, **kwargs):
        # Extrae el correo y la contraseña del cuerpo de la solicitud
        email = request.data.get('correo')
        password = request.data.get('contrasena')

        try:
            # Intenta obtener al usuario con el correo proporcionado
            usuario = Usuario.objects.get(correo=email)
        except Usuario.DoesNotExist:
            print("Usuario no encontrado")
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

        # Verificar la contraseña
        print("Contraseña almacenada en la base de datos:", usuario.contrasena)
        if not check_password(password, usuario.contrasena):
            print("Contraseña incorrecta")
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

        # Genera tokens de acceso y refresco
        refresh = RefreshToken.for_user(usuario.usuario)  # Genera el token usando el usuario relacionado
        access_token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'cedula': usuario.cedula,
            'correo': usuario.correo,
        }

        # Obtiene y organiza los datos del usuario para devolverlos en la respuesta
        user_data = {
            'cedula': usuario.cedula,
            'correo': usuario.correo,
            'compañías': [Compania.nombre for Compania in usuario.compañías.all()],
            'usuario_id': usuario.usuario.id,
        }

        return Response({'token': access_token, 'user_data': user_data}, status=status.HTTP_200_OK)

