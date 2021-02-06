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
            #print("Fetch all of the character data from our db")

            # retrieve the characters' slugs from the db
            characters = Character.objects.all()
            slugs = [character.slug for character in characters]
            #print("fetched {} characters".format(len(slugs)))


            if character not in slugs:
                #print("{} is not a valid argument".format(character))
                raise CommandError('Invalid argument')
            else:
                #print("character name ok")
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
        #print("About to request data from the source's API")
        endpoint = 'https://8wayrun.com/wiki/{}-frame-data-sc6/json'.format(character)
        response = requests.get(endpoint)

        if (response.status_code == 404):
            raise Http404()
        elif (response.status_code == 200):
            # response ok
            #print('200 - Successfully requested frame data')

            # get Character
            current_character = Character.objects.get(slug = character)

            # used to check duplicity and to check against the index number in the JSON response from the API
            commands = []
            i = 0
            for res in response.json():
                if (res.get('type') == 'fd6row'):
                    #print("{} - type check ok".format(i))
                    command = res.get('cmd') or None        # some res entries won't have a cmd, which means bad data
                    #print(command)
                    if command and command not in commands:
                        commands.append(command)
                        self.save_move(raw=res, character=current_character, index=i)
                i += 1

    def save_move(self, raw, character, index):
        # sample: raw = {'type': 'fd6row', 'atk': 'Laurier Cutter', 'cmd': ':A:', 'lvl': ':H:', 'dmg': '8', 'imp': '12', 'grd': '-6', 'hit': '2', 'cnt': '2'}
        #print(raw)

        section = self.get_section(command=raw.get('cmd'), character=character) or None

        #print("Section: ", section)

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

        #print(move)
        #print("Saving")    
        try:
            move.save()
            #print('Successfully saved the move entry into the database')
        except:
            #print("there was an error saving {} index from the JSON response into the database.".format(str(i)))
            raise CommandError('collect failed')

    def check_moves(self, character):
        current_character = Character.objects.get(slug = character)
        moves = Move.objects.filter(character=current_character, section=None)
        
        if (moves):
            #print("there are some Moves without a section that were collected")
            for move in moves:
                #print("- " , move)
        else:
            #print("There are no Moves without a section that were collected")



    # collaborators: this is a hard function to read, it also uses some very specific business logic from 8WayRun
    # business logic is explained here: https://8wayrun.com/wiki/controls-and-inputs/
    def get_section(self, command, character):
        # get every stance for the character
        stances = SpecialStance.objects.filter(character__name = character.name)
        stance_codes = [stance.abbreviation for stance in stances]
        
        # get every special state for the character
        states = SpecialState.objects.filter(character__name = character.name)
        state_codes = [state.abbreviation for state in states]

        section = None

        # these are characters placed at the beginning of a command that don't affect what section the command will be classified in
        # but are still allowed. Stand refers to the standing direction, ie Full Crouch, While Rising and Back Turned
        stand = "(FC\s)|(WR\s)|(BT\s)"   

        # sometimes wiki editors will write an entry with a command starting with ":LH: " or "LH " neither affects the section but still needs to be recognized
        noise = stand + "|(\:LH\:\s)|(LH\s)"   

        # some characters have "states" that also don't affect the section that move should fall under but may still appear
        # example Amy's RRP :A::A::A:, this move has RRP at the beginning of a horizontal attack
        for state_code in state_codes:
            noise += "|(" + state_code + "\s)"
        # seeing a ":d:" in a command input is saying that there is a direction
        # a move can have zero or more directions and will not affect the section, so long as it's not an 8-Way run 
        d = "(\:\d\:)|\*"
        button_a = "(\:A\:)|(\:a\-small\:)|(\:\(A\)\:)|(\:a.\:)|(\:a\(.\)\:)"
        button_b = "(\:B\:)|(\:b\-small\:)|(\:\(B\)\:)|(\:b.\:)|(\:b\(.\)\:)"
        button_k = "(\:K\:)|(\:k\-small\:)|(\:\(K\)\:)|(\:k.\:)|(\:k\(.\)\:)"
        # horizontal attacks are defined as having a "A" somewhere in the beggining of the command
        if (re.search("^((" + noise + ")*(" + d + ")*(" + button_a + "))", command)):
            section = "horizontal attack"

        # vertical attacks are defined as having a "B" somewhere in the beggining of the command
        if (re.search("^((" + noise + ")*(" + d + ")*(" + button_b + "))", command)):
            section = "vertical attack"

        # kicks are similar to vertical attacks and horizontal attacks
        if (re.search("^((" + noise + ")*(" + d + ")*(" + button_k + "))", command)):
            section = "kick attack"

        # dual button attacks are similar to horizontanl, vertical and kick attacks 
        # but they are combinations of A,B,K and G but not A+G or B+G or A+B+K
        if (re.search("(A\+B)|(B\+K)|(\:a-small\:\:\+\:\:b-small\:)|(A\+K)", command)):
            section = "dual button attack"

        # 8 way run refers to moving in any of the 8 directions in the game
        # in the commands it in the form :(d): where d is a digit and digits represent directions (see "directions" under "Basic Controls" here: 
        # https://8wayrun.com/wiki/controls-and-inputs/)
        if (re.search("(Run)|(\:\(\d\)\:)", command, re.IGNORECASE)): 
            section = "8-way run"

        # characters can be in "stances" when a stance is required to do a move, that move is a special move
        # characters may have zero or more stances, which is why we need to loop through each one
        for stance in stance_codes:
            if (re.search("^(" + noise + ")*" + stance, command)):
                section = "special move"
                break

        # throws are very simple, if they say "throw or if the input is A+G it's a throw"
        if (re.search("(throw)|(A\+G)", command, re.IGNORECASE)):
            section = "throw"
        # RE is similiar to a throw    
        if (re.search("(\:RE\:)|(B\+G)|(RE)", command, re.IGNORECASE)):
            section = "reversal attack"
        # gauge attacks are similar to throws and RE's
        if (re.search("(\:SC\:)|(\:A\+B\+K\:)|(SC)", command)):
            section = "gauge attack"
        

        # whichever section was assigned last to section is the section to assign on this move 
        # (sometimes a move may be assigned two or more sections while executing this method but there is precedence applied in this order:
        # gauge attacks, reversal attacks, throws, special moves, dual button attack, kick attack, vertical attack and horizontal attack)
        # that is why each if statement is independent of every other one and appear in the order that they do


        if (section):
            return Section.objects.get(name=section)
        else:
            return None
