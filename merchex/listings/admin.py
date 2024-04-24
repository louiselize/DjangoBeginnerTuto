
from django.contrib import admin

from listings.models import Band, Listings

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument


class ListingsAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('title','year') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Listings, ListingsAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
