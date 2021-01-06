from django.shortcuts import render
from django.http import HttpResponse
from .models import Character, Move, SpecialStance, Section, SpecialState
from django import template

register = template.Library()

allowable_images = [
    ":1:", ":2:", ":3:", ":4:", ":6:", ":7:", ":8:", ":9:",
    ":A:", ":B:", ":K:", ":G:",  
    ":A", "A:", ":B", "B:", "B", ":K", "K:", ":G", "G:",
    ":(1):", ":(2):", ":(3):", ":(4):", ":(6):", ":(7):", ":(8):", ":(9):",
    ":(A):", ":(B):", ":(K):", ":(G):",
    ":(A", "A):", ":(B", "B):", "(B)", ":(K", "K):", ":(G", "G):",
    "FC", "WR", "BT", "Run", "RUN",
    "*", "+", "(tip)", "Left side throw", "Right side throw", "Back throw",
    #":A+B:", ":(A+B):", ":a+b:", ":B+K:", ":(B+K):", ":b+k:", ":B+G:", ":(B+G):", ":b+g:", ":A+G:", ":(A+G):", ":a+g:", ":A+B+K:", 
    ":a:", ":b:", ":k:", ":g:",
    ":a", "a:", ":b", "b:", ":k", "k:", ":g", "g:",
    ":aB:", ":bA:", ":kA:", ":kB:",
    ":SC:", ":RE:"
]

def home(request):
    characters = Character.objects.all().order_by('name')

    context = {'characters': characters, 'title': 'Soulcalibur VI API'}
    return render(request, 'soulcalibur_vi/home.html', context)

def detail(request, slug):
    character = Character.objects.get(slug = slug)
    # order_by('id') is a trick I use to order objects in the ordder they were saved
    sections = Section.objects.all().order_by('id')     
    moves = Move.objects.filter(character=character).order_by('id')
    #print(len(moves))

    context = {
        "name": character.name,
        "image": character.image.url,
        "table_list": [],
        "title": character.name,
        "allowable_images": allowable_images,
    }

    for i in range(0, 9):
        context['table_list'].append({'table_name': sections[i].name, 'moves_list': []})
    context['sectionless_table'] = []

    for move in moves:
        #create a list of commands and height_levels from the respective strings so that I can use the for template tag on them
        command_string_to_list(move)
        height_level_string_to_list(move)

        if (move.section):
            if (move.section.name == "horizontal attack"):
                context['table_list'][0]['moves_list'].append(move)
            elif (move.section.name == "vertical attack"):
                context['table_list'][1]['moves_list'].append(move)
            elif (move.section.name == "kick attack"):
                context['table_list'][2]['moves_list'].append(move)
            elif (move.section.name == "dual button attack"):
                context['table_list'][3]['moves_list'].append(move)
            elif (move.section.name == "8-way run"):
                context['table_list'][4]['moves_list'].append(move)
            elif (move.section.name == "special move"):
                context['table_list'][5]['moves_list'].append(move)
            elif (move.section.name == "throw"):
                context['table_list'][6]['moves_list'].append(move)
            elif (move.section.name == "reversal attack"):
                context['table_list'][7]['moves_list'].append(move)
            elif (move.section.name == "gauge attack"):
                context['table_list'][8]['moves_list'].append(move)
        else:
            context['sectionless_table'].append(move)
    
    # for debugging: if len(moves) matches this next number, you did it right
    #print(len(context['table_list'][0]['moves_list']) + len(context['table_list'][1]['moves_list']) + len(context['table_list'][2]['moves_list']) + len(context['table_list'][3]['moves_list']) + len(context['table_list'][4]['moves_list']) + len(context['table_list'][5]['moves_list']) + len(context['table_list'][6]['moves_list']) + len(context['table_list'][7]['moves_list']) + len(context['table_list'][8]['moves_list']) + len(context['sectionless_table']))

    return render(request, 'soulcalibur_vi/character-detail.html', context)


def height_level_string_to_list(move):
    value = move.height_level
    height_level_list = []
    i = 0
    while (i < len(value)):
        if (value[i] == ":" and value[i+2] == ":"):
            height_level_list.append(value[i:i+3])
            i += 3
        elif (value[i] == ":" and value[i+3] == ":"):
            height_level_list.append(value[i:i+4])
            i += 4
        else:
            i += 1

    move.height_level = height_level_list

def command_string_to_list(move):
    value = move.command
    command_list = []
    i = 0
    while (i < len(value)):
        if (i + 15 < len(value) and value[i:i+16] in allowable_images):
            command_list.append(value[i:i+16])
            i += 16
        elif (i + 14 < len(value) and value[i:i+15] in allowable_images):
            command_list.append(value[i:i+15])
            i += 15
        elif (i + 9 < len(value) and value[i:i+10] in allowable_images):
            command_list.append(value[i:i+10])
            i += 10
        elif (i + 6 < len(value) and value[i:i+7] in allowable_images):
            command_list.append(value[i:i+7])
            i += 7
        elif (i + 5 < len(value) and value[i:i+6] in allowable_images):
            command_list.append(value[i:i+6])
            i += 6
        elif (i + 4 < len(value) and value[i:i+5] in allowable_images):
            command_list.append(value[i:i+5])
            i += 5
        elif (i + 3 < len(value) and value[i:i+4] in allowable_images):
            command_list.append(value[i:i+4])
            i += 4
        elif (i + 2 < len(value) and value[i:i+3] in allowable_images):
            command_list.append(value[i:i+3])
            i += 3
        elif (i + 1 < len(value) and value[i:i+2] in allowable_images):
            command_list.append(value[i:i+2])
            i += 2
        elif (value[i] in allowable_images):
            command_list.append(value[i])
            i += 1
        else:
            command_list.append(value[i])
            i += 1
    print(command_list)

    move.command = command_list
