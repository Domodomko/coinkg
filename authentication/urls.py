from django.urls import path, include
from authentication.views import UserActivationView

app_name = 'authentication'

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('users/activate/<slug:uid>/<slug:token>', UserActivationView.as_view(), name='activate'),


    # path('registration/', RegistrationAPIView.as_view(), name='registration'),
    # path('login/', LoginAPIView.as_view(), name='login'),
    # path('profile/', ProfileAPIView.as_view(), name='profile'),

]