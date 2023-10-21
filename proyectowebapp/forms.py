from django import forms
from .models import UserProfile  # Importa el modelo necesario

class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Asocia el formulario al modelo UserProfile
        fields = ['avatar']  # Lista los campos que deseas incluir en el formulario
