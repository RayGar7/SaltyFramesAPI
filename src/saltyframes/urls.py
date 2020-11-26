"""cfeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.contrib import admin


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    #re_path(r'^api/auth/', include(('accounts.api.urls', 'api-auth'), namespace='api-auth')),      # only for testing
    #re_path(r'^api/user/', include(('accounts.api.user.urls', 'api-user'), namespace='api-user')),
    re_path(r'^api/soulcalibur_vi/', include(('soulcalibur_vi.urls', 'soulcalibur_vi'), namespace='soulcalibur_vi')),
    #re_path(r'^api/status/', include(('status.api.urls', 'status'), namespace='api-status')),      # not ready for production
]
