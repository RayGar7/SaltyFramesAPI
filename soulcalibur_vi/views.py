from django.shortcuts import render
from django.http import HttpResponse
from .models import Character, Move, SpecialStance, Section, SpecialState

def home(request):
    characters = Character.objects.all().order_by('name')

    context = {'characters': characters, 'title': 'Soulcalibur VI API'}
    return render(request, 'soulcalibur_vi/home.html', context)


def detail(request, slug):
    character = Character.objects.get(slug = slug)
    sections = Section.objects.all().order_by('id')     # order_by('id') is a trick I use to order objects in the ordder they were saved
    moves = Move.objects.filter(character=character).order_by('id')
    #print(len(moves))

    # create a dictionary of arrays to create a frame data table, separated by the character's sections
    moves_table = {}
    for i in range(0, 9):
        moves_table[sections[i].name] = []
    moves_table['sectionless_table'] = []


    for move in moves:
        if (move.section):
            moves_table[move.section.name].append(move)
        else:
            moves_table['sectionless_table'].append(move)
    
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
        "sectionless_table": moves_table.get("sectionless_table"),
        "name": character.name
    }
    return render(request, 'soulcalibur_vi/character-detail.html', context)