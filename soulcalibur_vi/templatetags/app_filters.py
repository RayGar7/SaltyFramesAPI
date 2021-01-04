from django import template
from datetime import date, timedelta
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='newline')
def newline(value, arg):
    """ Adds a newline to the value once after every arg characters """
    # assert arg cannot be equal to zero: it will raise a division by zero excpetion and it also makes no sense
    # assert no negative characters
    new_value = ""
    for i in range(0, len(value)):
        new_value += value[i]
        if (i % arg == 0 and i != 0):
            # insert newline
            new_value += " "
            
    return new_value


@register.filter(name='height_level_to_image')
def height_level_to_image(value):
    """ Converts the height level string into an html formatted way of putting images inside the table cells """
    
    base_dir = "img/sc-attributes/"

    high = base_dir + "High.png"
    mid = base_dir + "Mid.png"
    low = base_dir + "Low.png"
    spec_low = base_dir + "SpecLow.png"
    spec_mid = base_dir + "SpecMid.png"
    ss = base_dir + "SS.png"
    gi = base_dir + "GI.png"


    new_value = ""
    i = 0
    length = len(value)
    while (i < length): 
        if (value[i:i+3] == ":H:"):
            new_value += high
            i += 3
        elif (value[i:i+3] == ":M:"):
            new_value += mid
            i += 3
        elif (value[i:i+3] == ":L:"):
            new_value += low
            i += 3
        elif (value[i:i+4] == ":SL:"):
            new_value += spec_low
            i += 4
        elif (value[i:i+4] == ":SM:"):
            new_value += spec_mid
            i += 4
        elif (value[i:i+4] == ":GI:"):
            new_value += gi
            i += 4
        elif (value[i:i+4] == ":SS:"):
            new_value += ss
            i += 4
        else:
            new_value += value[i]
            i += 1

    return new_value if len(new_value) else value

@register.filter(name='command_to_image')
def command_to_image(value):
    """ Converts the command string into an html formatted way of putting images inside the table cells """
    
    base_dir = "img/sc-inputs/"

    a = base_dir + "A.png"
    b = base_dir + "B.png"
    k = base_dir + "K.png"
    g = base_dir + "G.png"

    Ia = base_dir + "Ia.png"
    Ib = base_dir + "Ib.png"
    Ik = base_dir + "Ik.png"
    Ig = base_dir + "Ig.png"

    one = base_dir + "1.png"
    two = base_dir + "2.png"
    three = base_dir + "3.png"
    four = base_dir + "4.png"
    six = base_dir + "6.png"
    seven = base_dir + "7.png"
    eight = base_dir + "8.png"
    nine = base_dir + "9.png"

    Ione = base_dir + "I1.png"
    Itwo = base_dir + "I2.png"
    Ithree = base_dir + "I3.png"
    Ifour = base_dir + "I4.png"
    Isix = base_dir + "I6.png"
    Iseven = base_dir + "I7.png"
    Ieight = base_dir + "I8.png"
    Inine = base_dir + "I9.png"

    sc = base_dir + "SoulCharged.png"


    new_value = ""
    i = 0
    length = len(value)
    while (i < length): 
        if (value[i:i+3] == ":1:"):
            new_value += one
            i += 3
        elif (value[i:i+3] == ":2:"):
            new_value += two
            i += 3
        elif (value[i:i+3] == ":3:"):
            new_value += three
            i += 3
        elif (value[i:i+3] == ":4:"):
            new_value += four
            i += 3
        elif (value[i:i+3] == ":6:"):
            new_value += six
            i += 3
        elif (value[i:i+3] == ":7:"):
            new_value += seven
            i += 3
        elif (value[i:i+3] == ":8:"):
            new_value += eight
            i += 3
        elif (value[i:i+3] == ":9:"):
            new_value += nine
            i += 3

        elif (value[i:i+3] == ":A:"):
            new_value += a
            i += 3
        elif (value[i:i+3] == ":B:"):
            new_value += b
            i += 3
        elif (value[i:i+3] == ":K:"):
            new_value += k
            i += 3
        elif (value[i:i+3] == ":G:"):
            new_value += g
            i += 3

        elif (value[i:i+5] == ":(A):"):
            new_value += Ia
            i += 5
        elif (value[i:i+5] == ":(B):"):
            new_value += Ib
            i += 5
        elif (value[i:i+5] == ":(K):"):
            new_value += Ik
            i += 5
        elif (value[i:i+5] == ":(G):"):
            new_value += Ig
            i += 5

        elif (value[i:i+5] == ":(1):"):
            new_value += Ione
            i += 5
        elif (value[i:i+5] == ":(2):"):
            new_value += Itwo
            i += 5
        elif (value[i:i+5] == ":(3):"):
            new_value += Ithree
            i += 5
        elif (value[i:i+5] == ":(4):"):
            new_value += Ifour
            i += 5
        elif (value[i:i+5] == ":(6):"):
            new_value += Isix
            i += 5
        elif (value[i:i+5] == ":(7):"):
            new_value += Iseven
            i += 5
        elif (value[i:i+5] == ":(8):"):
            new_value += Ieight
            i += 5
        elif (value[i:i+5] == ":(9):"):
            new_value += Inine
            i += 5

        else:
            new_value += value[i]
            i += 1

    #print(new_value)

    return new_value if len(new_value) else value