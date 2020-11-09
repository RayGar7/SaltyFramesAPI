from ..models import Character
from rest_framework import serializers

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'version', 'date_time_version', 'source') # if not declared, all fields of the model will be shown
        
