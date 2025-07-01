from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog(request):
    print('blog')
    context = { 
        'text': 'Estamos no blog', 
        'title': 'Titulo do Blog'
    }

    return render(request, 'blog/index.html', context)

def exemplo(request):
    print('exemplo')

    context = { 
        'text': 'Estamos no exemplo', 
        'title': 'Titulo Exemplo do Blog'
    }
    return render(request, 'blog/exemplo.html', context)