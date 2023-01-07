from django.forms import ModelForm
from django import forms
from .models import *

class FormNegara(ModelForm):
    class Meta :
        model = Negara
        fields = '__all__'

        widgets = {
                'nama_negara' : forms.TextInput({'class':'form-control', 'required':'required'}),
                'letak_astronomi' :forms.TextInput({'class':'form-control', 'required':'required'}),
                'ibu_kota' :forms.TextInput({'class':'form-control', 'required':'required'}),
                'mata_uang' :forms.TextInput({'class':'form-control', 'required':'required'}),
                'bahasa_resmi' :forms.TextInput({'class':'form-control', 'required':'required'}),
                'bentuk_pemerintahan' :forms.TextInput({'class':'form-control', 'required':'required'}),
                'gambar' :forms.TextInput({'class':'form-control', 'required':'required'}), 
                'benua_id' :forms.Select({'class':'form-control', 'required':'required'})

        }

class FormKonservasi(ModelForm):
    class Meta :
        model = Konservasi
        fields = '__all__'

        widgets = {
                'nama_konservasi' : forms.TextInput({'class':'form-control', 'required':'required'}),
                'titik_koordinat' :forms.TextInput({'class':'form-control', 'required':'required'}),
                'letak_negara' :forms.TextInput({'class':'form-control', 'required':'required'}),
                
        }