from django import template

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
    spec_high = base_dir + "spechigh.png"
    ss = base_dir + "SS.png"
    gi = base_dir + "GI.png"
    th = base_dir + "TH.png"


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
        elif (value[i:i+4] == ":SH:"):
            new_value += spec_high
            i += 4
        elif (value[i:i+4] == ":GI:"):
            new_value += gi
            i += 4
        elif (value[i:i+4] == ":SS:"):
            new_value += ss
            i += 4
        elif (value[i:i+4] == ":TH:"):
            new_value += ss
            i += 4
        else:
            new_value += value[i]
            i += 1

    return new_value if len(new_value) else value

@register.filter(name='command_to_image')
def command_to_image(value):
    """ Converts the command string into an html formatted way of putting images inside the table cells """
    #print(value)
    base_dir = "img/sc-inputs/"

    new_value = ""

    my_dict = {
        ":1:": [base_dir + "1.png"],
        ":2:": [base_dir + "2.png"],
        ":3:": [base_dir + "3.png"],
        ":4:": [base_dir + "4.png"],
        ":6:": [base_dir + "6.png"],
        ":7:": [base_dir + "7.png"],
        ":8:": [base_dir + "8.png"],
        ":9:": [base_dir + "9.png"],


        ":A:": [base_dir + "A.png"],
        # ":A": base_dir + "A.png",
        # "A:": base_dir + "A.png",

        ":B:": [base_dir + "B.png"],
        # ":B": base_dir + "B.png",
        # "B:": base_dir + "B.png",

        ":K:": [base_dir + "K.png"],
        # ":K": base_dir + "K.png",
        # "K:": base_dir + "K.png",

        ":G:": [base_dir + "G.png"],
        # ":G": base_dir + "G.png",
        # "G:": base_dir + "G.png",


        ":A+B:": [base_dir + "A.png", base_dir + "B.png"],
        "A+B": [base_dir + "A.png", base_dir + "B.png"],


        ":(1):": [base_dir + "I1.png"],
        ":(2):": [base_dir + "I2.png"],
        ":(3):": [base_dir + "I3.png"],
        ":(4):": [base_dir + "I4.png"],
        ":(6):": [base_dir + "I6.png"],
        ":(7):": [base_dir + "I7.png"],
        ":(8):": [base_dir + "I8.png"],
        ":(9):": [base_dir + "I9.png"],


        ":(A):": [base_dir + "Ia.png"],
        # ":(A": base_dir + "Ia.png",
        # "A):": base_dir + "Ia.png",
        # ":(A)": base_dir + "Ia.png",
        # "(A):": base_dir + "Ia.png",

        ":(B):": [base_dir + "Ib.png"],
        # ":(B": base_dir + "Ib.png",
        # "B):": base_dir + "Ib.png",
        # ":(B)": base_dir + "Ib.png",
        # "(B):": base_dir + "Ib.png",

        ":(K):": [base_dir + "Ik.png"],
        # ":(K": base_dir + "Ik.png",
        # "K):": base_dir + "Ik.png",
        # ":(K)": base_dir + "Ik.png",
        # "(K):": base_dir + "Ik.png",

        ":(G):": [base_dir + "Ig.png"],
        # ":(G": base_dir + "Ig.png",
        # "G):": base_dir + "Ig.png",
        # ":(G)": base_dir + "Ig.png",
        # "(G):": base_dir + "Ig.png",


        ":SC:": [base_dir + "SoulCharged.png"],
        ":RE:": [base_dir + "RE.png"],
        "RE": [base_dir + "RE.png"],


        ":a-small:": [base_dir + "Sa.png"],
        # ":a-small": base_dir + "Sa.png",
        # "a-small:": base_dir + "Sa.png",

        ":b-small:": [base_dir + "Sb.png"],
        # ":b-small": base_dir + "Sb.png",
        # "b-small:": base_dir + "Sb.png",

        ":k-small:": [base_dir + "Sk.png"],
        # ":k-small": base_dir + "Sk.png",
        # "k-small:": base_dir + "Sk.png",

        ":g-small:": [base_dir + "Sg.png"],
        # ":g-small": base_dir + "Sg.png",
        # "g-small:": base_dir + "Sg.png",

        ":a:": [base_dir + "Sa.png"],
        # ":a": base_dir + "Sa.png",
        # "a:": base_dir + "Sa.png",

        ":b:": [base_dir + "Sb.png"],
        # ":b": base_dir + "Sb.png",
        # "b:": base_dir + "Sb.png",

        ":k:": [base_dir + "Sk.png"],
        # ":k": base_dir + "Sk.png",
        # "k:": base_dir + "Sk.png",

        ":g:": [base_dir + "Sg.png"],
        # ":g": base_dir + "Sg.png",
        # "g:": base_dir + "Sg.png",

        ":aB:": [base_dir + "M.png"],
        ":bA:": [base_dir + "N.png"],
        ":kA:": [base_dir + "O.png"],
        ":kB:": [base_dir + "P.png"],


        "*": [base_dir + "_notation.png"],
        "+": [base_dir + "plus.png"],
        ":+:": [base_dir + "plus.png"],
    }

    if (value in my_dict.keys()):
        #print(my_dict[value])
        return my_dict[value]
    else:
        return value