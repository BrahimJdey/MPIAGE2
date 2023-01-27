from django.contrib import admin
from .models import *

# # Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Fournisseur)
admin.site.register(Type)
admin.site.register(Facture)
admin.site.register(Produit)
# admin.site.register(Booking)
