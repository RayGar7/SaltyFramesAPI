from django.shortcuts import render
from django.http import HttpResponse
from .models import Character, Move, SpecialStance, Section, SpecialState
from django import template

register = template.Library()

#these strings can be turned into images
allowable_images = [
    ":1:", ":2:", ":3:", ":4:", ":6:", ":7:", ":8:", ":9:",
    ":A:", ":B:", ":K:", ":G:",  
    ":A", "A:", ":B", "B:", ":K", "K:", ":G", "G:",
    ":(1):", ":(2):", ":(3):", ":(4):", ":(6):", ":(7):", ":(8):", ":(9):",
    ":(A):", ":(B):", ":(K):", ":(G):",
    ":(A", "A):", ":(B", "B):", "(B)", ":(K", "K):", ":(G", "G):",
    ":(A)", "(A):", "(A", "A)", ":(B)", "(B):", "(B", "B)", ":(K)", "(K):", "(K", "K)",  ":(G)", "(G):", "(G", "G)",
    "FC", "WR", "BT", "Run", "RUN", "8WR",
    "*", "+", ":+:", "(tip)", "(Close Range)",
    "Left side throw", "Right side throw", "Back throw", "Left Side Throw", "Right Side Throw", "Back Throw", "Left Side", "Left side",
    "Back", "Air",
    ":a-small:", ":b-small:", ":k-small:", ":g-small:",
    ":a-small", "a-small:", ":b-small", "b-small:", ":k-small", "k-small:", ":g-small", "g-small:",
    ":a:", ":b:", ":k:", ":g:",
    ":a", "a:", ":b", "b:", ":k", "k:", ":g", "g:",
    ":aB:", ":bA:", ":kA:", ":kB:",
    ":SC:", ":RE:", "RE",
    ":M:", ":H:", ":L:", ":SM:", ":SH:", ":SL:",
]

def home(request):
    characters = Character.objects.all().order_by('name')

    context = {'characters': characters, 'title': 'Soulcalibur VI API'}
    return render(request, 'soulcalibur_vi/home.html', context)

def detail(request, slug):
    character = Character.objects.get(slug = slug)
    # order_by('id') is a trick I use to order objects in the order they were saved
    sections = Section.objects.all().order_by('id')     
    moves = Move.objects.filter(character=character).order_by('id')
    special_stances = SpecialStance.objects.filter(character=character)
    special_states = SpecialState.objects.filter(character=character)
    special_stance_abbreviations = [special_stance.abbreviation for special_stance in special_stances]
    special_state_abbreviations = [special_state.abbreviation for special_state in special_states]
    allowable_patterns = special_stance_abbreviations + special_state_abbreviations

    context = {
        "name": character.name,
        "image": character.image.url,
        "table_list": [],
        "title": character.name,
        "allowable_images": allowable_images,
        "allowable_patterns": allowable_patterns,
    }

    for i in range(0, 9):
        context['table_list'].append({'table_name': sections[i].name, 'moves_list': []})
    context['sectionless_table'] = []

    for move in moves:
        #create a list of commands and height_levels from the respective strings so that I can use the for template tag on them
        command_string_to_list(move=move, additional_patterns = allowable_patterns)
        height_level_string_to_list(move=move)

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
            
    return render(request, 'soulcalibur_vi/character-detail.html', context)

#helpers
def height_level_string_to_list(move):
    if (move.height_level):
        value = move.height_level
        height_level_list = []
        i = 0
        while (i < len(value)):
            if (i + 2 < len(value) and value[i:i+3] in allowable_images):
                height_level_list.append(value[i:i+3])
                i += 3
            elif (i + 3 < len(value) and value[i:i+4] in allowable_images):
                height_level_list.append(value[i:i+4])
                i += 4
            else:
                i += 1

        move.height_level = height_level_list
    else:
        move.height_level = []

def command_string_to_list(move, additional_patterns):
    value = move.command
    command_list = []

    # for pattern in additional_patterns:
    #     allowable_images.append(pattern)


    i = 0
    while (i < len(value)):

        #special case
        if (i + 6 < len(value) and value[i:i+7] == ":A+B+K:"):
            command_list.append(":A:")
            command_list.append(":+:")
            command_list.append(":B:")
            command_list.append(":+:")
            command_list.append(":K:")
            i += 7
        elif (i + 8 < len(value) and value[i:i+9] == ":(A+B+K):"):
            command_list.append(":(A):")
            command_list.append(":+:")
            command_list.append(":(B):")
            command_list.append(":+:")
            command_list.append(":(K):")
            i += 9

        if (i + 15 < len(value) and value[i:i+16] in allowable_images):
            command_list.append(value[i:i+16])
            i += 16
        elif (i + 14 < len(value) and value[i:i+15] in allowable_images):
            command_list.append(value[i:i+15])
            i += 15
        elif (i + 13 < len(value) and value[i:i+14] in allowable_images):
            command_list.append(value[i:i+14])
            i += 14
        elif (i + 12 < len(value) and value[i:i+13] in allowable_images):
            command_list.append(value[i:i+13])
            i += 13
        elif (i + 11 < len(value) and value[i:i+12] in allowable_images):
            command_list.append(value[i:i+12])
            i += 12
        elif (i + 10 < len(value) and value[i:i+11] in allowable_images):
            command_list.append(value[i:i+11])
            i += 11
        elif (i + 9 < len(value) and value[i:i+10] in allowable_images):
            command_list.append(value[i:i+10])
            i += 10
        elif (i + 8 < len(value) and value[i:i+9] in allowable_images):
            command_list.append(value[i:i+9])
            i += 9
        elif (i + 7 < len(value) and value[i:i+8] in allowable_images):
            command_list.append(value[i:i+8])
            i += 8
        elif (i + 6 < len(value) and value[i:i+7] in allowable_images):
            command_list.append(value[i:i+7])
            i += 7
        elif (i + 5 < len(value) and value[i:i+6] in allowable_images):
            command_list.append(value[i:i+6])
            i += 6
        elif (i + 4 < len(value) and value[i:i+5] in allowable_images or value[i:i+5] in additional_patterns):
            command_list.append(value[i:i+5])
            i += 5
        elif (i + 3 < len(value) and value[i:i+4] in allowable_images or value[i:i+4] in additional_patterns):
            command_list.append(value[i:i+4])
            i += 4
        elif (i + 2 < len(value) and value[i:i+3] in allowable_images or value[i:i+3] in additional_patterns):
            command_list.append(value[i:i+3])
            i += 3
        elif (i + 1 < len(value) and value[i:i+2] in allowable_images or value[i:i+2] in additional_patterns):
            command_list.append(value[i:i+2])
            i += 2
        elif (i >= len(value)):
            break
        elif (value[i] in allowable_images):
            command_list.append(value[i])
            i += 1
            #if this case happens it means that i was incremented in such a way that value[i] would raise IndexError
        else:
            command_list.append(value[i])
            i += 1

    move.command = command_list
