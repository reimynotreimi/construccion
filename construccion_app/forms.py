from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'tarea': forms.Select(attrs={
                'class': 'uiverse-input',
            })
        }

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        if not cedula.isdigit():
            raise forms.ValidationError("La cédula debe contener solo números.")
        if len(cedula) != 11:
            raise forms.ValidationError("La cédula debe tener exactamente 11 dígitos.")
        return cedula