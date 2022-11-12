from django.forms import ModelForm
from django import forms
from .models import Publicacao
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class PublicacaoForm(ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Titulo:', 'class': 'titulo', 'name': 'titulo'})) 
    conteudo_publicacao = forms.CharField(widget=SummernoteWidget()) 
    class Meta:
        model = Publicacao
        fields = ['titulo', 'imagem_publicacao', 'conteudo_publicacao', 'descricao_publicacao']