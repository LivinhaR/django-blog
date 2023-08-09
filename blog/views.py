from django.shortcuts import render

from blog.models import Post

# Create your views here.

from django.http import HttpResponse

def index(request):
    # return HttpResponse('Olá Django - index')
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})

def ola(request): # Modificar
    # return HttpResponse('Olá django')
    posts = Post.objects.all() # recupera todos os posts do banco de dados
    context = {'posts_list': posts } # cria um dicionário com os dado
    return render(request, 'posts.html', context) # renderiza o template e passa o contexto
