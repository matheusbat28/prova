from django.shortcuts import render, redirect
from .forms import PublicacaoForm
from .models import Publicacao

def cadastroPublicacao(request):
    contexto = {
        'form': PublicacaoForm
    }
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        img = request.FILES.get('imagem_publicacao')
        descricao = request.POST.get('descricao_publicacao')
        conteudo = request.POST.get('conteudo_publicacao')

        Publicacao.objects.create(titulo = titulo,
                                conteudo_publicacao = conteudo,
                                imagem_publicacao = img,
                                descricao_publicacao = descricao,
                                autor = request.user)
        return redirect('home')
    else:
        return render(request, 'cadastrarPost/index.html', context=contexto)
