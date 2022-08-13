from django.contrib import admin
from django import forms
from . import models
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = models.Movie
        fields = '__all__'


class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    form = MovieAdminForm



admin.site.register(models.Category)
admin.site.register(models.Actor, ActorAdmin)
admin.site.register(models.Genre)
admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.MovieShorts)
admin.site.register(models.RatingStar)
admin.site.register(models.Rating)
admin.site.register(models.Review)
admin.site.register(models.Treller)
