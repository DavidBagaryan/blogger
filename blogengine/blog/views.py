from django.shortcuts import render


def posts_list(request):
    names = ['ole', 'ksu', 'masha', 'ola']
    return render(request, 'blog/index.html', {'title': 'new title', 'names': names})
