from django.shortcuts import render
from django.http import HttpResponse
from .models import Character, Move, SpecialStance, Section, SpecialState
from django import template

register = template.Library()

def home(request):
    characters = Character.objects.all().order_by('name')

    context = {'characters': characters, 'title': 'Soulcalibur VI API'}
    return render(request, 'soulcalibur_vi/home.html', context)

def detail(request, slug):
    character = Character.objects.get(slug = slug)
    sections = Section.objects.all().order_by('id')     # order_by('id') is a trick I use to order objects in the ordder they were saved
    moves = Move.objects.filter(character=character).order_by('id')
    #print(len(moves))

    context = {
        "name": character.name,
        "image": character.image.url,
        "table_list": [],
        "title": character.name
    }

    for i in range(0, 9):
        context['table_list'].append({'table_name': sections[i].name, 'moves_list': []})
    context['sectionless_table'] = []

    for move in moves:
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
