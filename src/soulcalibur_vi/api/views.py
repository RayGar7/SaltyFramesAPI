
from ..models import Character
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response

class CharacterListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = serializers.CharacterSerializer
