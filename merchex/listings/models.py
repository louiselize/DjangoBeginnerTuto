from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)    
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

class Listings(models.Model):

    class Type(models.TextChoices):
        CD = "CD"
        VINYL = "VN"
        CASSETTE = "CS"
        DIGITAL = "DG"
        OTHER = "OT"

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="Enter a description")
    sold = models.BooleanField(default=False)
    year = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)],
        null=True
    )
    type = models.fields.CharField(Type.choices, max_length=3, default=Type.OTHER)