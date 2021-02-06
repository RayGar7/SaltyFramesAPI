from django import template

register = template.Library()


@register.filter(name='newline')
def newline(value, arg):
    """ Adds a newline to the value once after every arg characters """

    assert (arg > 0)
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
    height_dict = {
        ":H:": base_dir + "High.png",
        ":M:": base_dir + "Mid.png",
        ":L:": base_dir + "Low.png",
        ":SL:": base_dir + "SpecLow.png",
        ":SM:": base_dir + "SpecMid.png",
        ":SH:": base_dir + "spechigh.png",
        ":GI:": base_dir + "GI.png",
        ":SS:": base_dir + "SS.png",
        ":TH:": base_dir + "TH.png",

    }

    # this is way faster than looping through every key to see if the value is in height_dict as a key
    # it says return height_dict[value] if value exists as a key in height_dict, else return value as is
    return height_dict.setdefault(value, value) 


@register.filter(name='command_to_image')
def command_to_image(value):
    """ Converts the command string into an html formatted way of putting images inside the table cells """
    base_dir = "img/sc-inputs/"
    command_dict = {
        ":1:": base_dir + "1.png",
        ":2:": base_dir + "2.png",
        ":3:": base_dir + "3.png",
        ":4:": base_dir + "4.png",
        ":6:": base_dir + "6.png",
        ":7:": base_dir + "7.png",
        ":8:": base_dir + "8.png",
        ":9:": base_dir + "9.png",

        ":A:": base_dir + "A.png",
        ":B:": base_dir + "B.png",
        ":K:": base_dir + "K.png",
        ":G:": base_dir + "G.png",

        ":A+B:": base_dir + "AplusB.png",

        ":(1):": base_dir + "I1.png",
        ":(2):": base_dir + "I2.png",
        ":(3):": base_dir + "I3.png",
        ":(4):": base_dir + "I4.png",
        ":(6):": base_dir + "I6.png",
        ":(7):": base_dir + "I7.png",
        ":(8):": base_dir + "I8.png",
        ":(9):": base_dir + "I9.png",

        ":(A):": base_dir + "Ia.png",
        ":(B):": base_dir + "Ib.png",
        ":(K):": base_dir + "Ik.png",
        ":(G):": base_dir + "Ig.png",

        ":SC:": base_dir + "SoulCharged.png",
        ":RE:": base_dir + "RE.png",
        "RE": base_dir + "RE.png",

        ":a-small:": base_dir + "Sa.png",
        ":b-small:": base_dir + "Sb.png",
        ":k-small:": base_dir + "Sk.png",
        ":g-small:": base_dir + "Sg.png",

        ":a:": base_dir + "Sa.png",
        ":b:": base_dir + "Sb.png",
        ":k:": base_dir + "Sk.png",
        ":g:": base_dir + "Sg.png",
        
        ":aB:": base_dir + "M.png",
        ":bA:": base_dir + "N.png",
        ":kA:": base_dir + "O.png",
        ":kB:": base_dir + "P.png",

        "*": base_dir + "_notation.png",
        "+": base_dir + "plus.png",
        ":+:": base_dir + "plus.png",
    }

    return command_dict.setdefault(value, value)
