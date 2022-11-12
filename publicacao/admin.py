from django.contrib import admin
from .models import Publicacao
from django_summernote.admin import SummernoteModelAdmin 

class PublicacaoAdmin(SummernoteModelAdmin):
    list_display = ['titulo', 'autor', 'data_publicacao', ]
    list_display_links = ['titulo']
    search_fields = ['titulo', 'autor']
    summernote_fields = ['conteudo_publicacao',]

admin.site.register(Publicacao, PublicacaoAdmin)

