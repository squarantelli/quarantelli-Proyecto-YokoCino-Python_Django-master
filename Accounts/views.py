from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from Accounts.forms import *
from Accounts.models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def login_request(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(reverse('Inicio'))
        else:
            return render(request, 'Accounts/login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'Accounts/login.html')
    
"""
login_request es la view para el login
* utiliza authenticate que recibe user y password desde el html
* si el usuario no es None procede a iniciar la sesion
* caso contrario muestra un mensaje de error
"""

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"YokoCino/inicio.html")
    else:
        form = UserRegisterForm()     
    return render(request,"Accounts/register.html" ,  {"form":form})

"""
haciendo uso de UserRegisterForm, register es la vista que permite el registro de un nuevo usuario
* checkea que el form sea valido, limpia la data y guarda el contenido para luego renderizar inicio nuevamente
> el usuario debe iniciar sesion a mano luego
"""

def logout_request(request):
    logout(request)
    return redirect(reverse('Inicio'))

"""
view simple de cierre de sesion
"""

@login_required  
def profile(request):
    avatar_url = getavatar(request)
    return render(request, 'Accounts/profile.html',{'usuario': request.user, 'avatar_url': avatar_url})

"""
profile trae el la informacion completa de usuario y el avatar del mismo
"""

@login_required
def profileEdit(request):
    usuario = request.user
    avatar_url = getavatar(request)
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.save()

            user_link, _ = UserLink.objects.get_or_create(user=usuario)
            user_link.descripcion = informacion['descripcion']
            user_link.link = informacion['link']
            user_link.save()
            return render(request, "YokoCino/inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "Accounts/profileEdit.html", {"miFormulario": miFormulario, "usuario": usuario,"avatar_url":avatar_url})

"""
profileEdit permite editarlo en caso de querer realizar una modificacion
* trae en la variable usuario el user cn sesion activa
* checkea si el formulario es valido para pasar la informacion a una variable y luego descomponerla
* tambien trae o crea los campos extras de UserLink con la variable user_link
> Desconozco si existe mejor manera, pero fue la solucion que encontre para los campos extra que pide la entrega
"""

@login_required
def addAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarForm(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['avatar'])
            avatar.save()
            return render(request,"YokoCino/inicio.html")
    else:
        miFormulario = AvatarForm()
    return render(request,"Accounts/addAvatar.html",{'miFormulario':miFormulario})

"""
addAvatar agrega un avatar personalizado para el usuario activo
* usa el formulario simple AvatarForm, trae el username y lo guarda en la variable u
* pasa la data que se ingrese al formulario junto con el usuario para guardarlas luego
"""

def getavatar(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar:
        avatar_url = avatar.imagen.url
    else:
        avatar_url = None
    return avatar_url

"""
getavatar trae el avatar del usuario activo
* Actualmente se utiliza solo a la hora de ver el perfil
"""

@login_required
def sendMessage(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return render(request,'YokoCino/inicio.html')
    else:
        form = MessageForm()    
    return render(request, 'Accounts/sendMessage.html', {'form': form})

"""
sendMessage utiliza el formulario MessageForm para crear un nuevo mensaje
* checkea si el formulario es valido y lo guarda
* establece que el remitente es el usuario activo
* por ultimo guarda el mensaje en la base de datos y devuelve al inicio
"""

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'Accounts/inbox.html', {'messages': messages})

"""
inbox genera la bandeja de entrada 
* filtra entre todos los objetos Message por los que tengan al usuario activo como destinatario
* los ordena por timestamp
* muestra todos los mensajes uno detras del otro
> esta funcionalidad es la ultima implementada, hay mucho espacio de mejora futura
"""