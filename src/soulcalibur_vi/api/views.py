from __future__ import unicode_literals
from ..models import Character
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response




class CharacterListView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()


class MoveListView(generics.ListCreateAPIView):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer


class MoveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoveSerializer
    queryset = Move.objects.all()