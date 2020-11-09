import requests
from django.http import Http404
from .models import Character, FrameDataEntry




def add_one(character):
    endpoint = 'https://8wayrun.com/wiki/{}-frame-data-sc6/json'.format(character)
    response = requests.get(endpoint)
    if (response.status_code == 404):
        raise Http404()
    elif (response.status_code == 200):
        # response ok
        # save response data into the database
        for el in response.json():
            if (el.get('type') == 'fd6row'):
                # add to database
                pass

            

    sample = response.json()[2]
    print(sample)

def add_for_all():
    characters = ['amy']
    # for each item in characters you would then do what add_one() is doing.


#add_one('amy')

#how to use models inside of here:
   #Read ALL entries
objects = Character.objects.all()
res ='Printing all Dreamreal entries in the DB : '

for elt in objects:
    print(elt.name)