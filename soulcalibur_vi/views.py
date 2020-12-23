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
    
    # create a decoupled dict
    context = {
        "moves_table": moves_table,
        "horizontal_table": moves_table.get("horizontal attack"),
        "vertical_table": moves_table.get("vertical attack"),
        "kick_table": moves_table.get("kick attack"),
        "dual_button_table": moves_table.get("dual button attack"),
        "8_way_run_table": moves_table.get("8-way run"),
        "special_move_table": moves_table.get("special move"),
        "throw_table": moves_table.get("throw"),
        "reversal_attack_table": moves_table.get("reversal attack"),
        "gauge_attack_table": moves_table.get("gauge attack"),
        "name": character.name
    }
    print(context.keys())
    return render(request, 'soulcalibur_vi/character.html', context)