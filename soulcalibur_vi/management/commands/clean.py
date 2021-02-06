from django.core.management.base import BaseCommand, CommandError
from soulcalibur_vi.models import Character, Move


class Command(BaseCommand):
    help = 'Deletes all of the moves for a given character'

    def add_arguments(self, parser):
        parser.add_argument('character_slug')

    def handle(self, *args, **options):
        try:
            character_slug = options.get("character_slug")
            characters = Character.objects.all()
            slugs = [character.slug for character in characters]


            if character_slug not in slugs:
                raise CommandError('Invalid argument')
            else:
                self.clean_one(character_slug=character_slug)
                self.stdout.write(self.style.SUCCESS('Every move from the character: {} was deleted.'.format(character_slug)))

        except Exception:
            raise CommandError('clean failed')

    def clean_one(self, character_slug):
        character = Character.objects.get(slug=character_slug)
        moves = Move.objects.filter(character=character)
        moves.delete()