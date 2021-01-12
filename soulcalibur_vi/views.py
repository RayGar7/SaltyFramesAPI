from django.shortcuts import render
from django.http import HttpResponse
from .models import Character, Move, SpecialStance, Section, SpecialState
from django import template
from django.utils.safestring import mark_safe

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

    key = get_key()

    context = {
        'characters': characters, 
        'inputs': key['inputs'],
        'columns': key['columns'],
        'title': 'Soulcalibur VI API'
    }

    return render(request, 'soulcalibur_vi/home.html', context)

def legend(request):
    key = get_key()

    context = {'inputs': key['inputs'], 'columns': key['columns'], 'title': "Legend"}

    return render(request, 'soulcalibur_vi/legend.html', context)


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
