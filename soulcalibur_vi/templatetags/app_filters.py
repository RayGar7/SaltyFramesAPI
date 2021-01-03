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


@register.filter(name='height_level_to_image', is_safe=True)
def height_level_to_image(value):
    """ Converts the string into an html formatted way of putting images inside the table cells """
    
    print(value)
    #high = "img/sc-attributes/High.png"
    base_dir = "img/sc-attributes/"

    high = base_dir + "High.png"
    mid = base_dir + "Mid.png"
    low = base_dir + "Low.png"
    spec_low = base_dir + "SpecLow.png"
    spec_mid = base_dir + "SpecMid.png"
    ss = base_dir + "SS.png"


    # new_value = ""
    # i = 0
    # while (i < len(value)):        
    #     if (value[i:i+3] == ":H:"):
    #         new_value += high
    #         i += 3
    #     else:
    #         pass

    # print("new value: ")    
    # print(new_value)        
    # return mark_safe(new_value)
    return mark_safe(high)
