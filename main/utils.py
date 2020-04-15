from main.serializers import *
from django.core.paginator import Paginator
from django.shortcuts import render


def newslistpage(request):
    posts = News.objects.all()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,
                  'main/news_list.html',
                  {'news': posts})