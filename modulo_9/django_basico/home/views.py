from django.shortcuts import render

# Create your views here.

def home(request):
    print('home')

    context = { 
        'text': 'Estamos na home',
        'title': 'Titulo da Home'
    }

    return render(
        request, 
        'home/index.html',
        context
    )