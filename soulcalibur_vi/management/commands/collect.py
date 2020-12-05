from django.core.management.base import BaseCommand, CommandError
import requests, re
from django.http import Http404

from ...models import Character, Move, SpecialStance, Section, SpecialState



class Command(BaseCommand):
    help = 'Request the data from the source and save it into our own datbase'

    def handle(self, *args, **options):
        try:
            character = options.get("character_name")
            self.stdout.write(self.style.WARNING("About to collect data for {}".format(character)))
            print("Fetch all of the character data from our db")

            # retrieve the characters' slugs from the db
            characters = Character.objects.all()
            slugs = []
            for character_db in characters:
                slugs.append(character_db.slug)
            print("fetched {} characters".format(len(slugs)))


            if character not in slugs:
                print("{} is not a valid argument".format(character))
                raise CommandError
            else:

                print("character name ok")
                self.collect_one(character)
                self.stdout.write(self.style.SUCCESS('Every move was collected like a boss'))

                # check if there were any Move entries left without a section after running collect
                self.check_moves(character)

        except Exception:
            raise CommandError('collect failed')

    def add_arguments(self, parser):
        # Positional arguments are standalone name
        parser.add_argument('character_name')

    # todo check for duplicate Move entry's
    def collect_one(self, character):
        print("About to request data from the source's API")
        endpoint = 'https://8wayrun.com/wiki/{}-frame-data-sc6/json'.format(character)
        response = requests.get(endpoint)

        if (response.status_code == 404):
            raise Http404()
        elif (response.status_code == 200):
            # response ok
            print('200 - Successfully requested frame data')

            # get Character
            current_character = Character.objects.get(slug = character)

            # used to check duplicity
            #todo: we need to use querysets for this
            commands = []

            i = 0
            for res in response.json():
                if (res.get('type') == 'fd6row'):
                    print("{} - type check ok".format(i))
                    command = res.get('cmd')
                    if command not in commands:
                        commands.append(command)
                        self.save_move(raw=res, character=current_character)
                i += 1

    def save_move(self, raw, character):
        # sample: raw = {'type': 'fd6row', 'atk': 'Laurier Cutter', 'cmd': ':A:', 'lvl': ':H:', 'dmg': '8', 'imp': '12', 'grd': '-6', 'hit': '2', 'cnt': '2'}
        print(raw)
        
        # if (self.get_section(command=raw.get('cmd'), character=character)):
        #     section = self.get_section(command=raw.get('cmd'), character=character)
        # else:
        #     section = None

        section = self.get_section(command=raw.get('cmd'), character=character) or None

        print("Section: ", section)

        move = Move(character = character, 
        source = "8WayRun",
        section = section, 
        frames_to_impact = raw.get('imp'), 
        base_damage = raw.get('dmg'), 
        attack_name = raw.get('atk'), 
        command = raw.get('cmd'), 
        soulcharge_chip_damage = raw.get('chip'), 
        height_level = raw.get('lvl'), 
        recovery_on_guard = raw.get('grd'), 
        recovery_on_hit = raw.get('hit'), 
        recovery_on_counter_hit = raw.get('cnt'), 
        guard_burst_damage = raw.get('gb'), 
        notes = raw.get('nts')
        )

        print(move)
        print("Saving")    
        move.save()
        print('Successfully saved the move entry into the database')

    def check_moves(self, character):
        current_character = Character.objects.get(slug = character)
        moves = Move.objects.filter(character=current_character, section=None)
        
        if (moves):
            print("there are some Moves without a section that were collected")
            for move in moves:
                print("- " , move)
        else:
            print("There are no Moves without a section that were collected")


    # todo: need to account for if a character has RE in the notes
    # note to other devs: this is a hard function to read, it also uses some very specific business logic from 8wayrun
    def get_section(self, command, character):
        # get every stance for the character
        stances = SpecialStance.objects.filter(character__name = character.name)
        stance_codes = []
        for stance in stances:
            stance_codes.append(stance.abbreviation) 
        
        # get every special state for the character
        states = SpecialState.objects.filter(character__name = character.name)
        state_codes = []
        for state in states:
            state_codes.append(state.abbreviation) 


        result = None
        result_section = None

        stand = "(FC\s)|(WR\s)|(BT\s)"
        for state_code in state_codes:
            stand += "|(" + state_code + "\s)"

        d = "(\:\d\:)|\*"
        button_a = "(\:A\:)|(\:a\-small\:)|(\:\(A\)\:)|(\:a.\:)|(\:a\(.\)\:)"
        button_b = "(\:B\:)|(\:b\-small\:)|(\:\(B\)\:)|(\:b.\:)|(\:b\(.\)\:)"
        button_k = "(\:K\:)|(\:k\-small\:)|(\:\(K\)\:)|(\:k.\:)|(\:k\(.\)\:)"
        if (re.search("^((" + stand + ")*(" + d + ")*(" + button_a + "))", command)):
            result = "horizontal attack"
        if (re.search("^((" + stand + ")*(" + d + ")*(" + button_b + "))", command)):
            result = "vertical attack"
        if (re.search("^((" + stand + ")*(" + d + ")*(" + button_k + "))", command)):
            result = "kick attack"
        if (re.search("(A\+B)|(B\+K)|(\:a-small\:\:\+\:\:b-small\:)", command)):
            result = "dual button attack"
        if (re.search("(Run)|(\:\(\d\)\:)", command)): 
            result = "8-way run"
        for stance in stance_codes:
            if (re.search("^(" + stand + ")*" + stance, command)):
                result = "special move"
                break
        if (re.search("(throw)|(A\+G)", command)):
            result = "throw"
        if (re.search("(\:RE\:)|(B\+G)", command)):
            result = "reversal attack"
        if (re.search("(\:SC\:)|(\:A\+B\+K\:)|(SC)", command)):
            result = "gauge attack"
        
        if (result):
            result_section = Section.objects.get(name=result)

        return result_section
