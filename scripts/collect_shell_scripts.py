# import requests
# from soulcalibur_vi.models import Character, Move
# current_character = Character.objects.get(slug_source = 'seong-mi-na')
# endpoint = 'https://8wayrun.com/wiki/seong-mi-na-frame-data-sc6/json'
# response = requests.get(endpoint):A+B+K:

# res = response.json()[15]

# entry = Move(character = current_character, source = "8WayRun", type_entry = None, frames_to_impact = res.get('imp'), base_damage = res.get('dmg'), attack_name = res.get('atk'), command = res.get('cmd'), soulcharge_chip_damage = res.get('chip'), height_level = res.get('lvl'), recovery_on_guard = res.get('grd'), recovery_on_hit = res.get('hit'), recovery_on_counter_hit = res.get('cnt'), guard_burst_damage = res.get('gb'), notes = res.get('nts'))
# entry.save()

# for res in response.json():
#     if (res.get('type') != 'fd6end' and res.get('type') != 'fd6str' and res.get('type') != 'charsml'):
#         print(res.get('cmd'))

# current_character = Character.objects.get(name = 'Amy')
# entry = Move(character = current_character, source = "8WayRun", type_entry = None, frames_to_impact = res.get('imp'), base_damage = res.get('dmg'), attack_name = res.get('atk'), command = res.get('cmd'), soulcharge_chip_damage = res.get('chip'), height_level = res.get('lvl'), recovery_on_guard = res.get('grd'), recovery_on_hit = res.get('hit'), recovery_on_counter_hit = res.get('cnt'), guard_burst_damage = res.get('gb'), notes = res.get('nts'))


# # shell script to clear the database's Move entries
# from soulcalibur_vi.models import Character
# characters = Character.objects.all()
# characters.delete()

# failed at json entry 122 or 123

# import requests
from soulcalibur_vi.models import Character, Move
current_character = Character.objects.get(slug_source = 'astaroth')
res = {'type': 'fd6row', 'atk': 'Bringer of Ruin', 'cmd': 'SC :1::A::A:', 'lvl': ':L::L:', 'dmg': '65', 'imp': '36', 'grd': '-24', 'hit': 'KND', 'cnt': 'KND', 'gb': '5%', 'nts': 'NC'}
entry = Move(character = current_character, source = "8WayRun", section = None, frames_to_impact = res.get('imp'), base_damage = res.get('dmg'), attack_name = res.get('atk'), command = res.get('cmd'), soulcharge_chip_damage = res.get('chip'), height_level = res.get('lvl'), recovery_on_guard = res.get('grd'), recovery_on_hit = res.get('hit'), recovery_on_counter_hit = res.get('cnt'), guard_burst_damage = res.get('gb'), notes = res.get('nts'))
entry.save()



# script to test provide_section
from soulcalibur_vi.management.commands.collect import get_section
from soulcalibur_vi.models import Character, SpecialStance, Section, SpecialState
current_character = Character.objects.get(slug_source = 'amy')
#get_section('WRP BP :A:', current_character)



# test saving a move

from soulcalibur_vi.models import Character, SpecialStance, Section, Move
move = Move.objects.all()[0]
character = Character.objects.get(slug_source = 'seong-mi-na')

move = Move(character = character, 
source = "8WayRun",
section = None, 
frames_to_impact = move.frames_to_impact, 
base_damage = move.base_damage, 
attack_name = move.attack_name, 
command = move.command, 
soulcharge_chip_damage = move.soulcharge_chip_damage, 
height_level = move.height_level, 
recovery_on_guard = move.recovery_on_guard, 
recovery_on_hit = move.recovery_on_hit, 
recovery_on_counter_hit = move.recovery_on_hit, 
guard_burst_damage = move.guard_burst_damage, 
notes = move.notes
)


# shell script to drop Move entries for characters with failure in them
# hard-code the slug-source
from soulcalibur_vi.models import Character, Move
character = Character.objects.get(name="Inferno")
moves = Move.objects.filter(character=character)
moves.delete()



# shell script to test when save_move fails:
from soulcalibur_vi.management.commands.collect import get_section, save_move
from soulcalibur_vi.models import Character, SpecialStance, Section, Move, SpecialState
current_character = Character.objects.get(slug_source = 'groh')
save_move({'type': 'fd6row', 'atk': 'Guard', 'cmd': ':G:', 'lvl': 'n/a', 'dmg': 'n/a', 'chip': 'n/a', 'imp': 'n/a', 'grd': 'n/a', 'hit': 'n/a', 'cnt': 'n/a', 'gb': 'n/a'}, current_character)


# shell script to retrieve Moves without a section
# hard-code the slug-source
from soulcalibur_vi.models import Character, SpecialStance, Section, Move, SpecialState
current_character = Character.objects.get(slug_source = 'cervantes')
moves = Move.objects.filter(section=None)
moves_character = Move.objects.filter(character=current_character, section=None)
sections = Section.objects.all()
