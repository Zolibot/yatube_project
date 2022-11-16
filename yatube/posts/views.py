from django.shortcuts import render
from .models import Post


# Create your views here.
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Группы'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'content': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context)


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    # Словарь с данными принято называть context
    context = {
        'posts': posts,
    }
    return render(request, template, context)
