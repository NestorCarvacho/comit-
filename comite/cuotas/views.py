from django.shortcuts import render, redirect
from .models import *
from .form import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
    cuotas_presona = CuotaPersona.objects.all()
    ultima_cuota = Cuota.objects.latest('id_cuota')
    datos={
        'cuotas_persona': cuotas_presona,
        'ultima_cuota': ultima_cuota
    }
    return render(request, 'core/index.html', datos)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('administrar-cuota-persona')  #use redireccionar a google para la prueba solamente
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def administracionCuotaPersona(request):
    cuotas_presona = CuotaPersona.objects.all()
    ultima_cuota = Cuota.objects.latest('id_cuota')
    datos={
        'cuotas_persona': cuotas_presona,
        'ultima_cuota': ultima_cuota
    }
    return render(request, 'core/administrar-cuotas.html', datos)

####################################################################################################
@login_required
@permission_required('auth.view_user')
def crearCuotaPersona(request):
    if request.method == 'POST':
        form = CuotaPersonaFormAdd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('administrar-cuota-persona')
    else:
        form = CuotaPersonaFormAdd()
    return render(request, 'core/crear-cuota-persona.html', {'form': form})

@login_required
@permission_required('auth.view_user')
def editarCuotaPersona(request, id_cuota_persona):
    # Obtiene el producto correspondiente al id_producto proporcionado, o muestra un error 404 si no existe
    cuota_persona = get_object_or_404(CuotaPersona, id_cuota_persona=id_cuota_persona)
    if request.method == 'POST':
        # Si se recibe una solicitud POST, crea un formulario de Producto con los datos recibidos y la instancia del producto existente
        form = CuotaPersonaFormMod(request.POST, request.FILES, instance=cuota_persona)
        if form.is_valid():
            # Si el formulario es válido, guarda los cambios en el producto en la base de datos
            form.save()
            # Redirecciona a la vista 'listar_productos'
            return redirect('administrar-cuota-persona')
    else:
        # Si no es una solicitud POST, crea un formulario de Producto con la instancia del producto existente
        form = CuotaPersonaFormMod(instance=cuota_persona)
    # Renderiza la plantilla 'editar_producto.html' y pasa el formulario y el producto como contexto
    return render(request, 'core/modificar-cuota-persona.html', {'form': form, 'cuota_persona': cuota_persona})

@login_required
@permission_required('auth.view_user')
def eliminarCuotaPersona(request, id_cuota_persona):
    # Obtiene el producto correspondiente al id_producto proporcionado, o muestra un error 404 si no existe
    cuota_persona = get_object_or_404(CuotaPersona, id_cuota_persona=id_cuota_persona)
    if request.method == 'POST':
        # Si se recibe una solicitud POST, elimina el producto de la base de datos
        cuota_persona.delete()
        # Redirecciona a la vista 'listar_productos'
        return redirect('administrar-cuota-persona')
    # Renderiza la plantilla 'eliminar_producto.html' y pasa el producto como contexto
    return render(request, 'core/eliminar-cuota-persona.html', {'cuota_persona': cuota_persona})