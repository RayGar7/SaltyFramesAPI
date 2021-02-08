from django.core.management.base import BaseCommand, CommandError
from soulcalibur_vi.models import Character, Move


class Command(BaseCommand):
    help = 'Deletes all of the moves for a given character. Be very careful when you do this. Be sure that it\'s what you want to do.'

    def add_arguments(self, parser):
        parser.add_argument('character_slug')

    def handle(self, *args, **options):
        try:
            character_slug = options.get("character_slug")
            slugs = Character.objects.values_list('slug', flat=True)

            if (character_slug in slugs):
                self.clean_one(character_slug=character_slug)
                self.stdout.write(self.style.SUCCESS('Every move from the character: {} was deleted.'.format(character_slug)))
            elif (character_slug == "all"):
                self.clean_all()
                self.stdout.write(self.style.SUCCESS('Every move for every character has been deleted'))
            else:
                raise CommandError('Invalid argument')

        except Exception:
            raise CommandError('Clean failed')

    def clean_one(self, character_slug):
        character = Character.objects.get(slug=character_slug)
        moves = Move.objects.filter(character=character)
        moves.delete()

    def clean_all(self):
        moves = Move.objects.all()
        moves.delete()

        