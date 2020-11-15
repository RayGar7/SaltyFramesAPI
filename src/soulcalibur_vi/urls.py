from django.urls import re_path
from . import views
from .api import views

urlpatterns = [
    re_path(r'^$', views.CharacterListView.as_view(), name='list')
]