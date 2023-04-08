from django.contrib import admin
from .models import Cuisine, Restaurant


@admin.register(Cuisine)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Restaurant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('title', 'cuisine')
    list_filter = ('cuisine',)
