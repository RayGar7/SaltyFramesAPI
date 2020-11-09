from django.core.management.base import BaseCommand, CommandError
import requests
from django.http import Http404

from ...models import Character, FrameDataEntry


class Command(BaseCommand):
    help = 'Request the data from the source and save it into our own datbase'

    def handle(self, *args, **options):

        try:
            self.stdout.write(self.style.WARNING("About to request data from the source's API"))
            self.add_one('astaroth')

        except Exception:
            raise CommandError('Failed to request and save the data into the database')

    def add_one(self, character):
        endpoint = 'https://8wayrun.com/wiki/{}-frame-data-sc6/json'.format(character)
        response = requests.get(endpoint)

        if (response.status_code == 404):
            raise Http404()
        elif (response.status_code == 200):
            # response ok
            self.stdout.write(self.style.SUCCESS('Successfully requested frame data'))

            # get Character
            character_name = character[0].upper() + character[1:] # amy -> Amy
            current_character = Character.objects.get(name = character_name)

            i = 0
            for res in response.json():
                if (res.get('type') != 'fd6end' and res.get('type') != 'fd6str' and res.get('type') != 'charsml'):
                    print("{} - type check ok".format(i))
                    # add to database
                    # {'type': 'fd6row', 'atk': 'Laurier Cutter', 'cmd': ':A:', 'lvl': ':H:', 'dmg': '8', 'imp': '12', 'grd': '-6', 'hit': '2', 'cnt': '2'}
                    entry = FrameDataEntry(character = current_character, 
                    type_entry = None, 
                    frames_to_impact = res.get('imp'), 
                    base_damage = res.get('dmg'), 
                    attack_name = res.get('atk'), 
                    command = res.get('cmd'), 
                    soulcharge_chip_damage = res.get('chip'), 
                    height_level = res.get('lvl'), 
                    recovery_on_guard = res.get('grd'), 
                    recovery_on_hit = res.get('hit'), 
                    recovery_on_counter_hit = res.get('cnt'), 
                    guard_burst_damage = res.get('gb'), 
                    notes = res.get('nts')
                    )

                    print("Saving")
                    entry.save()
                else:
                    # todo: change the 'type' of the move
                    pass
                i += 1


    def update_one(self, character):
        endpoint = 'https://8wayrun.com/wiki/{}-frame-data-sc6/json'.format(character)
        response = requests.get(endpoint)

        if (response.status_code == 404):
            raise Http404()
        elif (response.status_code == 200):
            # response ok
            self.stdout.write(self.style.SUCCESS('Successfully requested frame data'))

            # get Character
            character_name = character[0].upper() + character[1:] # amy -> Amy
            current_character = Character.objects.get(name = character_name)

            i = 0
            for res in response.json():
                if (res.get('type') != 'fd6end' and res.get('type') != 'fd6str' and res.get('type') != 'charsml'):
                    print("{} - type check ok".format(i))
                    # add to database
                    # {'type': 'fd6row', 'atk': 'Laurier Cutter', 'cmd': ':A:', 'lvl': ':H:', 'dmg': '8', 'imp': '12', 'grd': '-6', 'hit': '2', 'cnt': '2'}
                    entry = FrameDataEntry(character = current_character, type_entry = None, frames_to_impact = res.get('imp'), base_damage = res.get('dmg'), attack_name = res.get('atk'), command = res.get('cmd'), soulcharge_chip_damage = res.get('chip'), height_level = res.get('lvl'), recovery_on_guard = res.get('grd'), recovery_on_hit = res.get('hit'), recovery_on_counter_hit = res.get('cnt'), guard_burst_damage = res.get('gb'), notes = res.get('nts'))

                    print("Saving")
                    entry.save()
                else:
                    pass
                i += 1




# shell scripts


# import requests
# from soulcalibur_vi.models import Character, FrameDataEntry
# endpoint = 'https://8wayrun.com/wiki/astaroth-frame-data-sc6/json'
# response = requests.get(endpoint)
# res = response.json()[210]
# current_character = Character.objects.get(name = 'Astaroth')
# entry = FrameDataEntry(character = current_character, type_entry = None, frames_to_impact = res.get('imp'), base_damage = res.get('dmg'), attack_name = res.get('atk'), command = res.get('cmd'), soulcharge_chip_damage = res.get('chip'), height_level = res.get('lvl'), recovery_on_guard = res.get('grd'), recovery_on_hit = res.get('hit'), recovery_on_counter_hit = res.get('cnt'), guard_burst_damage = res.get('gb'), notes = res.get('nts'))

