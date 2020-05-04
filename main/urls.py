from django.urls import path

from .views import *
from .utils import *


app_name = 'main'

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('successtory/', SuccessStoryListView.as_view(), name='success_story'),
    path('aboutus/', AboutUsListView.as_view(), name='about_us'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('feedback/', FeedBackCreateView.as_view(), name='feedback'),
    path('credit/', CreditListCreateView.as_view(), name='credit'),
    path('creditsinfo/', CreditsInfoListView.as_view(), name='credits_info'),

]