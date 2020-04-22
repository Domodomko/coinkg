from django.core.paginator import Paginator
from django.shortcuts import render
from .serializers import *


def newslistpage(request):
    posts = News.objects.all()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    # return render(request,
    #               'main/news_list.html',
    #               {'news': posts})