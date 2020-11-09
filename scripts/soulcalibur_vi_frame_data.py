import requests
from django.http import Http404
# import soulcalibur_vi model 

# # I will have to run one of these for every character
# response = requests.get('https://8wayrun.com/wiki/amy-frame-data-sc6/json')
# if (response.status_code == 404):
#     raise Http404()
# elif (response.status_code == 200):
#     # response ok
#     #print(response.json())
#     #print(type(response.json()))
#     # once I have the data and I know its type I have to saveit into the database
#     for el in response.json():
#         pass
#         #print(el)
#         #print(type(el))
#         # every element in response.json() is a dict
#         # now how should this be saved into the database with the Model API?
#         #print(el.keys())

#     print(response.json()[2])
#     sample = response.json()[2]
#     #print(sample.keys())
#     for key in sample.keys():
#         print(key)

#     # from running that data I can see that it's more or less in this format: 
#     # 
#     # {'type': 'fd6str'}
#     # {'type': 'fd6row', 'atk': 'Laurier Cutter', 'cmd': ':A:', 'lvl': ':H:', 'dmg': '8', 'imp': '12', 'grd': '-6', 'hit': '2', 'cnt': '2'}
#     # {'type': 'fd6end'}


def add_one(character):
    endpoint = 'https://8wayrun.com/wiki/{}-frame-data-sc6/json'.format(character)
    response = requests.get(endpoint)
    if (response.status_code == 404):
        raise Http404()
    elif (response.status_code == 200):
        # response ok
        #print(response.json())
        #print(type(response.json()))
        # once I have the data and I know its type I have to saveit into the database
        for el in response.json():
            if (el.get('type') == 'fd6row'):
                # add to database

            

    sample = response.json()[2]
    print(sample)

def add_for_all():
    characters = ['amy']
    # for each item in characters you would then do what add_one() is doing.


add_one('amy')