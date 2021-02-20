from django.contrib import admin
from .models import Yoga, Guru, TrainingLevels


# admin.site.register(Yoga)
# admin.site.register(Trainer)
# admin.site.register(TrainingLevel)

@admin.register(Yoga)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'start_time', 'end_time', 'desc')
    list_filter = ('city', 'start_time', 'end_time')


@admin.register(Guru)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'yoga', 'exp')
    list_filter = ('yoga', 'exp')


@admin.register(TrainingLevels)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('training_name', 'yoga', 'training_type')
    list_filter = ('yoga', 'training_type')
