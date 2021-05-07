from django.contrib import admin

from .models import Pet, Vaccine


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'species', 'age', 'sex']


@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']