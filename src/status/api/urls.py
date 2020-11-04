#from django.conf.urls import url
from django.urls import path, re_path, include
from .views import (
    StatusAPIView, 
    StatusAPIDetailView,
    )

urlpatterns = [
    re_path(r'^$', StatusAPIView.as_view(), name='list'),
    re_path(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view(), name='detail'),
]



#Start with
# /api/status/ -> List
# /api/status/create -> Create
# /api/status/12/ -> Detail
# /api/status/12/update/ -> Update
# /api/status/12/delete/ -> Delete


# End With

# /api/status/ -> List -> CRUD
# /api/status/1/ -> Detail -> CRUD


# Final

# /api/status/ -> CRUD & LS 