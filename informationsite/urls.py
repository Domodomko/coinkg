from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

schema_view = get_schema_view(openapi.Info(
      title="Coin API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),)

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URL
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('api/main/', include('main.urls')),
    path('api/auth/', include('authentication.urls')),
    url(r'^$', TemplateView.as_view(template_name='list.html'), name='home'),
]
