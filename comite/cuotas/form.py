#form.py
from django import forms
from .models import *
from django.forms import ModelForm, widgets

class CuotaPersonaFormAdd(forms.ModelForm):
    class Meta:
        model = CuotaPersona
        fields = ['monto_cuota',
                  'fecha',
                  'estado',
                  'cuota',
                  'persona']
    def __init__(self, *args, **kwargs):
        super(CuotaPersonaFormAdd, self).__init__(*args, **kwargs)
        self.fields['cuota'].queryset = Cuota.objects.all()
        self.fields['persona'].queryset = Persona.objects.all()

class CuotaPersonaFormMod(forms.ModelForm):
    class Meta:
        model = CuotaPersona
        fields = ['monto_cuota',
                  'fecha',
                  'estado',
                  'cuota',
                  'persona']
        
        widgets = {
            'monto_cuota': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cuota': forms.Select(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(CuotaPersonaFormMod, self).__init__(*args, **kwargs)
        self.fields['cuota'].queryset = Cuota.objects.all()
        self.fields['persona'].queryset = Persona.objects.all()