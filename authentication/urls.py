from django.urls import path, include
from authentication.views import UserActivationView, AccountView

app_name = 'authentication'

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('users/activate/<slug:uid>/<slug:token>', UserActivationView.as_view(), name='activate'),
    path('account/', AccountView.as_view()),

]