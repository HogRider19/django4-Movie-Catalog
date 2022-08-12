from django.contrib import admin
from . import models


class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']



admin.site.register(models.Category)
admin.site.register(models.Actor, ActorAdmin)
admin.site.register(models.Genre)
admin.site.register(models.Movie)
admin.site.register(models.MovieShorts)
admin.site.register(models.RatingStar)
admin.site.register(models.Rating)
admin.site.register(models.Review)
admin.site.register(models.Treller)
