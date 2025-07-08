from django.http import HttpResponse, Http404
from blog.data import posts
from django.shortcuts import render
from typing import Any

# Create your views here.
def blog(request):
    print('blog')
    context = { 
        'text': 'Estamos no blog', 
        'title': 'Titulo do Blog',
        'posts': posts
    }

    return render(request, 'blog/index.html', context)

def exemplo(request):
    print('exemplo')

    context = { 
        'text': 'Estamos no exemplo', 
        'title': 'Titulo Exemplo do Blog',
    }
    return render(request, 'blog/exemplo.html', context)


def post(request, post_id):
    print('post')

    found_post: dict [str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não encontrado')

    context = { 
        'text': 'Estamos no post', 
        'title': found_post['title'] + ' - ',
        'post': found_post
    }

    return render(request, 'blog/post.html', context)