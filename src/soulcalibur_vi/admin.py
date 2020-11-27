from django.contrib import admin

from .models import Character, Move, SpecialStance, Section, SpecialState

admin.site.register(Character)
admin.site.register(Move)
admin.site.register(SpecialStance)
admin.site.register(Section)
admin.site.register(SpecialState)