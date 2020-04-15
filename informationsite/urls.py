from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from django.conf.urls import url

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URL
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('api/main/', include('main.urls')),
    path('api/auth/', include('authentication.urls')),
    url(r'^$', TemplateView.as_view(template_name='list.html'), name='home'),
]
