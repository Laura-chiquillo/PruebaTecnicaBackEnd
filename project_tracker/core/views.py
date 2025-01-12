from django.shortcuts import render
from .serializers import HistoriaDeUsuarioSerializer, TicketSerializer, UsuarioSerializer
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password
from .serializers import UsuarioSerializer

from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Usuario, Compania

def crear_historia(request):
    if request.method == 'POST':
        form = HistoriaDeUsuarioSerializer(request.POST)
        if form.is_valid():
            form.save()  # Guarda la nueva historia de usuario
            return HttpResponseRedirect('/exito/')  # Redirige a una página de éxito
    else:
        form = HistoriaDeUsuarioSerializer()
    
    return render(request, 'core/crear_historia.html', {'form': form})

def crear_ticket(request):
    if request.method == 'POST':
        form = TicketSerializer(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo ticket
            return HttpResponseRedirect('/exito/')
    else:
        form = TicketSerializer()

    return render(request, 'core/crear_ticket.html', {'form': form})

@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # Cifrar la contraseña antes de guardarla
        data['contrasena'] = make_password(data['contrasena'])
        
        serializer = UsuarioSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Usuario creado correctamente'}, status=201)
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)



def login_view(request):
    return render(request, 'core/login.html')

class CustomAuthToken(APIView):
    def post(self, request, *args, **kwargs):
        correo = request.data.get('correo')
        contrasena = request.data.get('contrasena')

        if not correo or not contrasena:
            return Response({'error': 'Correo y contraseña son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            usuario = Usuario.objects.get(correo=correo)
        except Usuario.DoesNotExist:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

        # Verificar la contraseña
        if not check_password(contrasena, usuario.contrasena):
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            # Generar el token
            refresh = RefreshToken.for_user(usuario)
            access_token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'cedula': usuario.cedula,
                'correo': usuario.correo,
            }

            user_data = {
                'cedula': usuario.cedula,
                'correo': usuario.correo,
                'compañías': [compania.nombre for compania in usuario.compania.all()],
            }

            return Response({'token': access_token, 'user_data': user_data}, status=status.HTTP_200_OK)

        except APIException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return Response({'error': 'Error desconocido', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)