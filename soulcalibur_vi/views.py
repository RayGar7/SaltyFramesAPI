from django.shortcuts import render
from django.http import HttpResponse
from .models import Character, Move, SpecialStance, Section, SpecialState

def home(request):
    characters = Character.objects.all().order_by('name')

    context = {'characters': characters, 'title': 'Soulcalibur VI API'}
    return render(request, 'soulcalibur_vi/home.html', context)


# def character_view(request):
#     print(request)
#     return HttpResponse(r"hello")
#     #character = Character.objects.get(source="")

def detail(request, slug):
    character = Character.objects.get(slug = slug)
    sections = Section.objects.all().order_by('id')
    moves = Move.objects.filter(character=character)
    #print(len(moves))

    # create a dictionary of arrays to create a frame data table, separated by the character's sections
    moves_table = {}
    for i in range(0, 9):
        moves_table[sections[i].name] = []


    for move in moves:
        moves_table[move.section.name].append(move)
    
    # for debugging: if len(moves) matches this next number, you did it right
    #print(len(moves_table[sections[0].name]) + len(moves_table[sections[1].name]) + len(moves_table[sections[2].name]) + len(moves_table[sections[3].name]) + len(moves_table[sections[4].name]) + len(moves_table[sections[5].name]) + len(moves_table[sections[6].name]) + len(moves_table[sections[7].name]) + len(moves_table[sections[8].name]))
    
    context = {
        "moves_table": moves_table,
        "name": character.name
    }
    return render(request, 'soulcalibur_vi/character.html', context)