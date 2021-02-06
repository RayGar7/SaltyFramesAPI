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


# O(1)
# assumes the caller of this function will always validate "value" as a key in height_dict
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

    return height_dict.get(value) 


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
        ":A+K:": base_dir + "AplusK.png",
        ":A+G:": base_dir + "AplusG.png",
        ":B+K:": base_dir + "BplusK.png",
        ":B+G:": base_dir + "BplusG.png",
        ":K+G:": base_dir + "KplusG.png",
        ":A+B+K:": base_dir + "AplusB.png",

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

        ":(A+B):": base_dir + "lapluslb.png",
        ":(A+K):": base_dir + "lapluslk.png",
        ":(A+G):": base_dir + "lapluslg.png",
        ":(B+K):": base_dir + "lbpluslk.png",
        ":(B+G):": base_dir + "lbpluslg.png",
        ":(K+G):": base_dir + "lkpluslg.png",
        ":(A+B+K):": base_dir + "lapluslbpluslk.png",

        ":SC:": base_dir + "SoulCharged.png",
        ":RE:": base_dir + "RE.png",
        "RE": base_dir + "RE.png",
        ":GI:": base_dir + "GI.png",

        ":a-small:": base_dir + "Sa.png",
        ":b-small:": base_dir + "Sb.png",
        ":k-small:": base_dir + "Sk.png",
        ":g-small:": base_dir + "Sg.png",

        ":a:": base_dir + "Sa.png",
        ":b:": base_dir + "Sb.png",
        ":k:": base_dir + "Sk.png",
        ":g:": base_dir + "Sg.png",
        
        ":aA:": base_dir + "aA.png",
        ":aB:": base_dir + "aB.png",
        ":aK:": base_dir + "aK.png",
        ":aG:": base_dir + "aG.png",

        ":bA:": base_dir + "bA.png",
        ":bB:": base_dir + "bB.png",
        ":bK:": base_dir + "bK.png",
        ":bG:": base_dir + "bG.png",
        
        ":kA:": base_dir + "kA.png",
        ":kB:": base_dir + "kB.png",
        ":kK:": base_dir + "kK.png",
        ":kG:": base_dir + "kG.png",

        ":gA:": base_dir + "gA.png",
        ":gB:": base_dir + "gB.png",
        ":gK:": base_dir + "gK.png",
        
        ":a(A):": base_dir + "ala.png",
        ":a(B):": base_dir + "alb.png",
        ":a(K):": base_dir + "alk.png",
        ":a(G):": base_dir + "alg.png",

        ":b(A):": base_dir + "bla.png",
        ":b(B):": base_dir + "blb.png",
        ":b(K):": base_dir + "blk.png",
        ":b(G):": base_dir + "blg.png",
        
        ":k(A):": base_dir + "kla.png",
        ":k(B):": base_dir + "klb.png",
        ":k(K):": base_dir + "klk.png",
        ":k(G):": base_dir + "klg.png",

        ":g(A):": base_dir + "gla.png",
        ":g(B):": base_dir + "glb.png",
        ":g(K):": base_dir + "glk.png",

        "*": base_dir + "_notation.png",
        "+": base_dir + "plus.png",
        ":+:": base_dir + "plus.png",
    }

    return command_dict.get(value)
