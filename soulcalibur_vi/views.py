from django.shortcuts import render
from django.http import HttpResponse
from .models import Character, Move, SpecialStance, Section, SpecialState

def home(request):
    characters = Character.objects.all()
    print(characters)

    context = {'characters': characters}
    return render(request, 'soulcalibur_vi/home.html', context)
