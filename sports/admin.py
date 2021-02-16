from django.contrib import admin
from .models import Academy, Sports, Coach


# admin.site.register(Academy)
# admin.site.register(Coach)
# admin.site.register(Sports)

@admin.register(Academy)
class AcademyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'start_time', 'end_time', 'desc')
    list_filter = ('city', 'start_time', 'end_time')


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'academy', 'exp')
    list_filter = ('academy', 'exp')


@admin.register(Sports)
class SportsAdmin(admin.ModelAdmin):
    list_display = ('sports_name', 'academy', 'sports_type')
    list_filter = ('academy', 'sports_type')
