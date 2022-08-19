from django import forms
from .models import Gezi
from django.forms import ModelForm

class BilgiFormu(forms.Form):
    isim = forms.CharField(max_length=100, label='İsminiz')
    eposta = forms.EmailField(required=False, label='Eposta Adresiniz')
    konu = forms.CharField(max_length=100, label="Konu")
    mesaj = forms.CharField(widget=forms.Textarea, label="Mesajınız")


class GeziFormu(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Gezi
        fields = [
            'adi', 'yer', 'bolge',
             'foto', 'ani'
        ]

