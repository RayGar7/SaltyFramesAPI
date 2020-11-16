from django.urls import re_path
from . import views
from .api import views

urlpatterns = [
    re_path(r'^api/characters/$', views.CharacterListView.as_view(), name='character_list'),
    re_path(r'^api/characters/(?P<pk>\d+)/$', views.CharacterView.as_view(), name='character_detail'),
    re_path(r'^api/moves/$', views.MoveListView.as_view(), name='move_list'),
    re_path(r'^api/moves/(?P<pk>\d+)/$', views.MoveView.as_view(), name='move_detail')
]