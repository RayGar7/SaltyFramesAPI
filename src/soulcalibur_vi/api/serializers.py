from ..models import Character, Move, Section
from rest_framework import serializers, fields





class MoveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Move
        fields = ('source', 'frames_to_impact', 'base_damage', 'attack_name', 'command', 'soulcharge_chip_damage', 'height_level', 'recovery_on_guard', 'recovery_on_hit', 'recovery_on_counter_hit', 'guard_burst_damage', 'notes') 


class CharacterSerializer(serializers.ModelSerializer):
    move_character = MoveSerializer(read_only=True, many=True)

    class Meta:
        model = Character
        fields = ('name', 'version', 'date_time_version', 'move_character') 

