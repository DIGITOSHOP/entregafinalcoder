from django.urls import path

from proyectowebapp import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
   
    path ('',views.home, name="Home"),
    path('profile/', views.user_profile, name='user_profile'),
   
    
        
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)