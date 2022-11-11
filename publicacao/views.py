from django.shortcuts import render


def cadastroPublicacao(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'cadastrarPost/index.html')
