from django.shortcuts import render
from django.http import HttpResponse
from .models import Character, Move, SpecialStance, Section, SpecialState
from django import template
from django.utils.safestring import mark_safe
from icecream import ic

register = template.Library()

#these strings can be turned into images
command_smilies = [
    ":1:", ":2:", ":3:", ":4:", ":6:", ":7:", ":8:", ":9:",
    ":(1):", ":(2):", ":(3):", ":(4):", ":(6):", ":(7):", ":(8):", ":(9):",
    ":A:", ":B:", ":K:", ":G:",  
    ":(A):", ":(B):", ":(K):", ":(G):",
    ":A+B:", ":A+K:", ":A+G:", ":B+K:", ":B+G:", ":K+G:", ":A+B+K:", ":(A+B+K):",
    ":(A+B):", ":(A+K):", ":(A+G):", ":(B+K):", ":(B+G):", ":(K+G):", 
    "*", "+", ":+:",
    ":a-small:", ":b-small:", ":k-small:", ":g-small:",
    ":a:", ":b:", ":k:", ":g:",
    ":aA:",":aB:",":aK:",":aG:",":a(A):",":a(B):",":a(K):", ":a(G):",
    ":bA:",":bB:",":bK:",":bG:",":b(A):",":b(B):",":b(K):",":b(G):",
    ":kA:",":kB:",":kK:",":kG:",":k(A):",":k(B):",":k(K):",":k(G):",
    ":gA:",":gB:",":gK:",":g(A):",":g(B):",":g(K):",
    ":SC:", ":RE:", "RE", ":GI:",
]


# these strings can be turned into images too
height_level_smilies = [
    ":M:", ":H:", ":L:", ":SM:", ":SH:", ":SL:", ":TH:", ":GI:", ":SS:"
]

def home(request):
    characters = Character.objects.all().order_by('name')

    key = get_key()

    context = {
        'characters': characters, 
        'inputs': key['inputs'],
        'columns': key['columns'],
        'title': 'Soulcalibur VI'
    }

    return render(request, 'soulcalibur_vi/home.html', context)

def legend(request):
    key = get_key()

    context = {'inputs': key['inputs'], 'columns': key['columns'], 'title': "Legend"}

    return render(request, 'soulcalibur_vi/legend.html', context)

def detail(request, slug):
    character = Character.objects.get(slug = slug)
    sections = Section.objects.all().order_by('id')     
    moves = Move.objects.filter(character=character).order_by('id')

    context = {
        "name": character.name,
        "image": character.image.url,
        "table_list": [],
        "title": character.name,
        "command_smilies": command_smilies,
        "height_level_smilies": height_level_smilies,
    }

    for i in range(0, 9):
        context['table_list'].append({'table_name': sections[i].name, 'moves_list': []})
    context['sectionless_table'] = []

    for move in moves:
        #create a list of commands and height_levels from the respective strings so that I can use the for template tag on them
        command_string_to_list(move=move)
        height_level_string_to_list(move=move)

        if (move.section):
            assign_section(section=move.section, context=context, move=move)
        else:
            context['sectionless_table'].append(move)
            
    return render(request, 'soulcalibur_vi/character-detail.html', context)

# Helpers

def assign_section(section, context, move):
    #  don't do it like this anymore, instead use Move.objects.filter()


    if (section.name == "horizontal attack"):
        context['table_list'][0]['moves_list'].append(move)
    elif (section.name == "vertical attack"):
        context['table_list'][1]['moves_list'].append(move)
    elif (section.name == "kick attack"):
        context['table_list'][2]['moves_list'].append(move)
    elif (section.name == "dual button attack"):
        context['table_list'][3]['moves_list'].append(move)
    elif (section.name == "8-way run"):
        context['table_list'][4]['moves_list'].append(move)
    elif (section.name == "special move"):
        context['table_list'][5]['moves_list'].append(move)
    elif (section.name == "throw"):
        context['table_list'][6]['moves_list'].append(move)
    elif (section.name == "reversal attack"):
        context['table_list'][7]['moves_list'].append(move)
    elif (section.name == "gauge attack"):
        context['table_list'][8]['moves_list'].append(move)

def get_key():
    base_dir = 'img/sc-inputs/'

    columns = [
        {
            'label': "Move",
            'message': mark_safe("English <strong>name</strong> of the move."),
        },
        {
            'label': "Command",
            'message': mark_safe("<strong>Input</strong> to execute move."),
        },
        {
            'label': "Level",
            'message': mark_safe("Describes the <strong>height level</strong> of the move."),
        },
        {
            'label': "IMP",
            'message': mark_safe("Frames to <strong>impact</strong> the amount of frames it takes a move to become active."),
        },
        {
            'label': "DMG",
            'message': mark_safe("<strong>Damage</strong> that will be dealt on hit."),
        },
        {
            'label': "GRD",
            'message': mark_safe("How many frames you will be in advantage or disadvantage if this move is <strong>blocked</strong>."),
        },
        {
            'label': "Hit",
            'message': mark_safe("How many frames you will be in advantage or disadvantage if this move <strong>hits</strong>."),
        },
        {
            'label': "CH",
            'message': mark_safe("How many frames you will be in advantage or disadvantage when landing a <strong>Counter Hit</strong>."),
        },
        {
            'label': "GB",
            'message': mark_safe("How much <strong>guard-burst damage</strong> the move will make."),
        },
        {
            'label': "Notes",
            'message': mark_safe("Additional <strong>Notes</strong>. Please note that the icon processing system hasn't been implemented in this version. That's why you will see notes with format like this: '	:GI::H::M: [8-20], +6 and 2 stacks towards Dark Legacy on successful GI' where the it is displayed in code separated by colons as opposed to using images. This will be fixed soon."),
        },
    ]

    inputs_without_images = [
        {
            'label': base_dir + '',
            'message': mark_safe("Press next input <strong>during guard or hit</strong> or activates <strong>on guard or hit</strong>."),
        },
        {
            'label': base_dir + '',
            'message': mark_safe("Activates on successful <strong>Guard Impact</strong>."),
        },
        {
            'label': base_dir + '',
            'message': mark_safe("Input needs to be executed <strong>fast</strong>."),
        },
        {
            'label': base_dir + '',
            'message': mark_safe("Activated when <strong>being hit while performing the move (revenge)</strong>."),
        },
        {
            'label': base_dir + '',
            'message': mark_safe("Versus a <strong>downed</strong> opponent."),
        },
        {
            'label': base_dir + '',
            'message': mark_safe("Versus a <strong>crouching</strong> opponent."),
        },
        {
            'label': base_dir + '',
            'message': mark_safe("Performed while being <strong>downed</strong>."),
        },
        {
            'label': base_dir + '',
            'message': mark_safe("Activated when the move connects <strong>close</strong>."),
        },
        {
            'label': base_dir + '',
            'message': mark_safe("Input the next button <strong>during motion</strong>(Geralt only)"),
        }
    ]

    inputs = [
        {
            'label': base_dir + '6.png',
            'message': mark_safe("White arrows indicate which direction to <strong>press</strong>."),
        },
        {
            'label': base_dir + 'I6.png',
            'message': mark_safe("Black arrows indicate which direction to <strong>press twice</strong>."),
        },
        {
            'label': base_dir + 'A.png',
            'message': mark_safe("<strong>Horizontal</strong> Attack.</p>"),
        },
        {
            'label': base_dir + 'B.png',
            'message': mark_safe("<p><strong>Vertical</strong> Attack.</p>"),
        },
        {
            'label': base_dir + 'K.png',
            'message': mark_safe("<strong>Kick</strong> Attack Move."),
        },
        {
            'label': base_dir + 'G.png',
            'message': mark_safe("<strong>Guard</strong> Move."),
        },
        {
            'label': base_dir + 'Ia.png',
            'message': mark_safe("Black letters will indicate which attack button to <strong>hold down</strong>."),
        },
        {
            'label': base_dir + 'Sa.png',
            'message': mark_safe("When a button is shown <strong>small</strong> it should be <strong>pressed briefly</strong> before moving on to the next input."),
        },
        {
            'label': base_dir + 'M.png',
            'message': mark_safe("When a small button is right next to a big button it means the button is supposed to be pressed immediately. This is equivalent to a small button followed by a big button even if there is some spcae between them."),
        },
        {
            'label': base_dir + '_notation.png',
            'message': mark_safe("The asterisk stands for <strong>OR</strong>."),
        },
        {
            'label': base_dir + 'AplusB.png',
            'message': mark_safe("The plus will indicate when you have to press multiple inputs <strong>together</strong>."),
        },
        {
            'label': base_dir + 'H.png',
            'message': mark_safe("The move behaves differently on <strong>counter hit</strong>."),
        },
        {
            'label': base_dir + 'FC.png',
            'message': mark_safe("The move is performed during <strong>full crouch</strong>."),
        },
        {
            'label': base_dir + 'BT.png',
            'message': mark_safe("The move is performed while being <strong>back turned</strong>."),
        },
        {
            'label': base_dir + 'WR.png',
            'message': mark_safe("The move is performed <strong>while rising</strong> from a crouch."),
        },
        {
            'label': base_dir + 'R.png',
            'message': mark_safe("The move is performed while <strong>running</strong>."),
        },
        {
            'label': base_dir + 'JMP.png',
            'message': mark_safe("The move is performed while <strong>jumping</strong>."),
        },
        {
            'label': base_dir + 'SoulCharged.png',
            'message': mark_safe("Move can only be executed while in <strong>Soul Charge</strong> mode."),
        },
        {
            'label': base_dir + 'RE.png',
            'message': mark_safe("Perform input after <strong>Reversal Edge Clash</strong>."),
        },
        {
            'label': base_dir + 'just.png',
            'message': mark_safe("Input needs to be a <strong>just input (input with exact timing)</strong>."),
        },
        {
            'label': base_dir + 'vsMidair.png',
            'message': mark_safe("Versus an <strong>airborne</strong> opponent."),
        },
        {
            'label': base_dir + 'eightWayRun.png',
            'message': mark_safe("During <strong>Eight-Way-Run</strong> movement."),
        },
    ]

    return {'columns': columns, 'inputs_without_images': inputs_without_images, 'inputs': inputs}


def get_allowable_patterns(character):
    special_stances = SpecialStance.objects.filter(character=character)
    special_stance_abbreviations = [special_stance.abbreviation for special_stance in special_stances]
    special_states = SpecialState.objects.filter(character=character)
    special_state_abbreviations = [special_state.abbreviation for special_state in special_states]
    
    return special_stance_abbreviations + special_state_abbreviations

def height_level_string_to_list(move):
    value = move.height_level
    if (value):
        height_level_list = []
        i = 0
        save_point = i
        while (i < len(value) - 1):
            if (value[i] == ":"):
                j = i + 1
                while(j < len(value)):
                    if (value[j] == ":"):
                        height_level_list.append(value[i:j+1])
                        i = j + 1
                        save_point = i
                        break
                    else:
                        j += 1
            else:
                i += 1
                if (i == len(value)):
                    height_level_list.append(value[save_point:i])
                elif (value[i] == ":"):
                    height_level_list.append(value[save_point:i])
        move.height_level = height_level_list
    else:
       move.height_level = ["-"]

def command_string_to_list(move):
    value = move.command
    command_list = []


    i = 0
    save_point = 0
    while (i < len(value) - 1):
        if (value[i] == ":" and not (value[i+1] == ":" or value[i+1] == " ")):
            j = i + 1
            while(j < len(value)):
                if (value[j] == ":"):
                    command_list.append(value[i:j+1])
                    i = j + 1
                    save_point = i
                    break
                else:
                    j += 1
        elif (value[i] == ":" and (value[i+1] == ":" or value[i+1] == " ")):
            command_list.append(value[i])
            i = i + 1
            save_point = i
        else:
            i += 1
            if (i == len(value) - 1):
                command_list.append(value[save_point:i+1])
            elif (value[i] == ":"):
                command_list.append(value[save_point:i])
                save_point = i

    move.command = command_list

