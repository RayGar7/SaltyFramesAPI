from django.urls import re_path, path
from . import views as views
from .api import views as api_views

app_name = 'soulcalibur_vi'
urlpatterns = [
    path('', views.home, name='home'),
    path('legend/', views.legend, name='legend'),
    #re_path(r'^characters/$', api_views.CharacterListView.as_view(), name='character_list'),
    #re_path(r'^characters/(?P<pk>\d+)/$', api_views.CharacterView.as_view(), name='character_detail'),
    #re_path(r'^moves/$', views.MoveListView.as_view(), name='move_list'),
    #re_path(r'^moves/(?P<pk>\d+)/$', views.MoveView.as_view(), name='move_detail')
    #path('<slug:slug>/', api_views.CharacterView.as_view(), name='character_detail'),
    re_path(r'^characters-api/(?P<pk>\d+)/$', api_views.CharacterRetrieveView.as_view(), name='character_public_detail'),
    #re_path(r'^character/(?P<pk>\d+)/$', views.character_view, name='character_detail'),
    # ex: /polls/5/
    #path('<int:character_id>/', views.detail, name='detail'),
    path('<slug:slug>/', views.detail, name='detail'),
]