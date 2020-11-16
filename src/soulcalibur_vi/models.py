from django.db import models
from datetime import datetime
from django.utils.timezone import now


class Character(models.Model):
    name = models.CharField(max_length=30, unique=True)

    # game version
    version = models.IntegerField(null=True, blank=True)

    # when the character was added to the database (my database - the Superframes database)
    date_time_db_entry = models.DateTimeField(auto_now=True)

    # when the character's frame data was updated by the source
    date_time_version = models.DateTimeField(editable=True)

    # every frame data page on the source for a character has a slug different from the name field. In the common case it's their first name in lower case but sometimes it's not
    slug_source = models.CharField(max_length=30, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name




class Move(models.Model):
    character = models.ForeignKey('Character', on_delete=models.CASCADE, related_name='move_character')

    # always credit the providers of the data
    source = models.CharField(max_length=30, default='8WayRun')

    section = models.ForeignKey('Section', on_delete=models.CASCADE, null=True, blank=True)

    frames_to_impact = models.CharField(max_length=30, null=True, blank=True)

    base_damage = models.CharField(max_length=30, null=True, blank=True)

    attack_name = models.CharField(max_length=60, null=True, blank=True)

    command = models.CharField(max_length=60, null=False, blank=False)

    soulcharge_chip_damage = models.CharField(max_length=30, null=True, blank=True)

    height_level = models.CharField(max_length=30, null=True, blank=True)

    recovery_on_guard = models.CharField(max_length=30, null=True, blank=True) # will need client side convesion to integer for features like font coloring

    recovery_on_hit = models.CharField(max_length=30, null=True, blank=True)

    recovery_on_counter_hit = models.CharField(max_length=30, null=True, blank=True)

    guard_burst_damage = models.CharField(max_length=30, null=True, blank=True)

    notes = models.TextField(max_length=240, null=True, blank=True)
    

    def __str__(self):
        return self.character.name + "\'s " + self.command or "No name"

class SpecialStance(models.Model):
    name = models.CharField(max_length=30)
    character = models.ForeignKey('Character', on_delete=models.CASCADE)
    abbreviation = models.CharField(max_length=30)

    def __str__(self):
        return self.character.name + "\'s " + self.name + " - (" + self.abbreviation + ")"

class Section(models.Model):
    name = models.CharField(max_length=40, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class SpecialState(models.Model):
    name = models.CharField(max_length=50)
    character = models.ForeignKey('Character', on_delete=models.CASCADE)
    abbreviation = models.CharField(max_length=30)

    def __str__(self):
        return self.name + " - (" + self.abbreviation + ")"