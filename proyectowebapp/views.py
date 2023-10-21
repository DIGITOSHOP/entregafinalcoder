from django.shortcuts import render, HttpResponse



# Create your views here.

def home (request):
     
     return render (request,"proyectowebapp/home.html")
 


def acerca (request):
     
     return render (request,"proyectowebapp/acerca.html")
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AvatarUploadForm  # Importa el formulario para la carga del avatar
from .models import UserProfile  # Importa el modelo de perfil de usuario

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = AvatarUploadForm(
            request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            avatar_anterior = UserProfile.objects.filter(user=request.user)
            if len(avatar_anterior) > 0:
                avatar_anterior.delete()
            avatar_nuevo = UserProfile(
                user=request.user, avatar=form.cleaned_data["avatar"])
            avatar_nuevo.save()
            print("is valid")
            # Redirige al perfil del usuario después de cargar el avatar
            return redirect('user_profile')
    else:
        form = AvatarUploadForm()

    return render(request, 'avatar/user_profile.html', {'form': form})






 

 
 