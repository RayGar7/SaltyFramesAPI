#from django.conf.urls import url
from django.urls import re_path

from .views import (
            UpdateModelDetailAPIView,
            UpdateModelListAPIView 
    )

app_name = 'updates.api'        # if this doesn't work try 'updates'
urlpatterns = [
    re_path(r'^$', UpdateModelListAPIView.as_view()), # api/updates/ - List/Create
    re_path(r'^(?P<id>\d+)/$', UpdateModelDetailAPIView.as_view()),
] 