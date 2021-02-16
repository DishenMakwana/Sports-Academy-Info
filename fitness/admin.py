from django.contrib import admin
from .models import Fitness, Trainer, TrainingLevel


# admin.site.register(Fitness)
# admin.site.register(Trainer)
# admin.site.register(TrainingLevel)

@admin.register(Fitness)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'start_time', 'end_time', 'desc')
    list_filter = ('city', 'start_time', 'end_time')


@admin.register(Trainer)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'fitness', 'exp')
    list_filter = ('fitness', 'exp')


@admin.register(TrainingLevel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('training_name', 'fitness', 'training_type')
    list_filter = ('fitness', 'training_type')
